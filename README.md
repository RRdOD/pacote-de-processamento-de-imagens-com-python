# Pacote de Processamento de Imagens em Python 🖼️📦

Este é um pacote simples de **processamento de imagens** desenvolvido em Python, utilizando a biblioteca [Pillow](https://python-pillow.org/). Ele permite realizar operações básicas como:

- Carregar uma imagem
- Converter para escala de cinza
- Redimensionar
- Aplicar desfoque (blur)
- Salvar imagem processada

## 📦 Requisitos

- Python 3.6 ou superior
- Pillow (instale com o comando abaixo)

```bash
pip install Pillow
```

## 📁 Arquivo principal

- `image_processing_package.py` → contém todas as funções e um exemplo de uso no final do script.

## ▶️ Como usar

1. Salve o arquivo `image_processing_package.py` no seu projeto.
2. Coloque uma imagem na mesma pasta com o nome `exemplo.jpg` ou altere o caminho no código.
3. Execute o script com:

```bash
python image_processing_package.py
```

Se tudo estiver certo, ele criará um novo arquivo chamado `saida_processada.jpg`, com a imagem em tons de cinza, redimensionada e com desfoque aplicado.

## 🧪 Funções disponíveis

| Função          | Descrição                                     |
|-----------------|-----------------------------------------------|
| `load_image()`  | Carrega uma imagem a partir do caminho        |
| `save_image()`  | Salva a imagem em um caminho especificado     |
| `to_grayscale()`| Converte para escala de cinza                 |
| `resize_image()`| Redimensiona para tamanho (largura, altura)   |
| `blur_image()`  | Aplica desfoque Gaussiano com raio definido   |
