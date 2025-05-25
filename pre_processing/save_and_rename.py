import os
import cv2

# Caminho das imagens de entrada e saída
input_folder = "image_dataset"
output_folder = "apple_dataset"

# Tamanho novo (exemplo: 200x200)
new_size = (256, 256)

# Criar a pasta de saída, se não existir
os.makedirs(output_folder, exist_ok=True)

def save_and_rename_imgs(prefix):
    # Iterar sobre as imagens
    folder = os.path.join(input_folder, prefix)
    for id, filename in enumerate(os.listdir(folder)):
        if filename.lower().endswith((".jpg")):
            img_path = os.path.join(folder, filename)
            
            # Ler imagem
            img = cv2.imread(img_path)
            
            if img is None:
                print(f"Unable to open: {img_path}")
                continue

            # Redimensionar imagem
            resized_img = cv2.resize(img, new_size, interpolation=cv2.INTER_AREA)

            # Novo nome: exemplo "imagem_1.jpg"
            new_name = f"{prefix}_apple{id}.jpg"
            output_path = os.path.join(output_folder, prefix, new_name)

            # Salvar a imagem
            cv2.imwrite(output_path, resized_img)

            print(f"Saved to: {output_path}")

if __name__ == "__main__":
    save_and_rename_imgs("ai")
    save_and_rename_imgs("real")
    print("All images saved and renamed")