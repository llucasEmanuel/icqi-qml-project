import os
import cv2
import numpy as np
from scipy.stats import entropy, circstd
from sklearn.preprocessing import MinMaxScaler
import pandas as pd

def get_image_params(image_path):
    img = cv2.imread(image_path)
    if img is None:
        print(f"Image not found: {image_path}")
        return None

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    f = np.fft.fft2(gray)
    fshift = np.fft.fftshift(f)
    magnitude = np.abs(fshift)

    media_magnitude = np.mean(magnitude)
    energia_total = np.sum(magnitude**2)
    maximo = np.max(magnitude)
    desvio_padrao = np.std(magnitude)

    mag_norm = magnitude.flatten()
    mag_norm = mag_norm / np.sum(mag_norm)
    entropia = entropy(mag_norm + 1e-8)

    # Redimensiona para 64x64 para manter padrão
    new_img = cv2.resize(img, (64, 64))

    # HLS para hue, lightness, saturation
    hls = cv2.cvtColor(new_img, cv2.COLOR_BGR2HLS)
    H = hls[..., 0].astype(np.float32).flatten() * 2  # Hue em 0-360
    L = hls[..., 1].astype(np.float32).flatten()
    S = hls[..., 2].astype(np.float32).flatten()

    # Chroma a partir do RGB
    B, G, R = cv2.split(new_img)
    B = B.astype(np.float32).flatten()
    G = G.astype(np.float32).flatten()
    R = R.astype(np.float32).flatten()

    max_rgb = np.maximum(np.maximum(R, G), B)
    min_rgb = np.minimum(np.minimum(R, G), B)
    C = max_rgb - min_rgb  # Chroma

    std_H = circstd(H, high=360, low=0)
    std_L = np.std(L)
    std_C = np.std(C)
    std_S = np.std(S)

    return {
        "fft_mean": media_magnitude,
        "fft_total_energy": energia_total,
        "fft_max": maximo,
        "fft_std": desvio_padrao,
        "fft_entropy": entropia,
        "std_hue": std_H,
        "std_chroma": std_C,
        "std_lightness": std_L,
        "std_saturation": std_S
    }


if __name__ == "__main__":
    results = {
        "fft_mean": [],
        "fft_total_energy": [],
        "fft_max": [],
        "fft_std": [],
        "fft_entropy": [],
        "std_hue": [],
        "std_chroma": [],
        "std_lightness": [],
        "std_saturation": [],
        "ai_gen": []
    }

    for i in range(150):
        img_path = os.path.join("apple_dataset", "ai", f"ai_apple{i}.jpg")
        params = get_image_params(img_path)
        if params is not None:
            for key in params:
                results[key].append(params[key])
            results["ai_gen"].append(1)

    for i in range(156):
        img_path = os.path.join("apple_dataset", "real", f"real_apple{i}.jpg")
        params = get_image_params(img_path)
        if params is not None:
            for key in params:
                results[key].append(params[key])
            results["ai_gen"].append(0)

    df = pd.DataFrame(results)

    scaler = MinMaxScaler(feature_range=(0, 100))
    cols_to_normalize = [col for col in df.columns if col != "ai_gen"]
    df[cols_to_normalize] = scaler.fit_transform(df[cols_to_normalize])

    CSV_PATH = "dataset_params.csv"
    df.to_csv(CSV_PATH, index=False)

    print(f"Parameters saved to {CSV_PATH}")
