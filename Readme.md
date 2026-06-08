# Show and Tell

[![Pylint](https://github.com/christopher-dabrowski/Show-and-Tell/actions/workflows/pylint.yml/badge.svg)](https://github.com/christopher-dabrowski/Show-and-Tell/actions/workflows/pylint.yml)

![GitHub commits since tagged version](https://img.shields.io/github/commits-since/christopher-dabrowski/Show-and-Tell/forked?style=for-the-badge&color=green)
![Python Version from PEP 621 TOML](https://img.shields.io/python/required-version-toml?tomlFilePath=https%3A%2F%2Fraw.githubusercontent.com%2Fchristopher-dabrowski%2FShow-and-Tell%2Frefs%2Fheads%2Fmaster%2Fpyproject.toml&style=for-the-badge&logo=python)

Projekt akademicki, którego celem jest poznanie algorytmu Show and Tell.
Projekt bazuje na pracy [Show and Tell: A Neural Image Caption Generator](https://arxiv.org/pdf/1411.4555.pdf) oraz repozytorium [a-PyTorch-Tutorial-to-Image-Captioning](https://github.com/sgrvinod/a-PyTorch-Tutorial-to-Image-Captioning).

Prezentacja działania, opis metody _Show and Tell_ oraz wybrane eksperymenty są przedstawione w [ShowAndTell_Demo.ipynb](ShowAndTell_Demo.ipynb).

Całość eksperymentów znjduej się w katalogu `eksperymenty`.

## Algorytm Show and Tell

Model Show and Tell jest jednym z pierwszych skutecznych podejść do automatycznego ge-
nerowania opisów tekstowych na podstawie obrazów. Architektura łączy sieć konwolucyjną, która
pełni rolę ekstraktora cech wizualnych, z siecią rekurencyjną odpowiedzialną za generowanie se-
kwencji słów opisujących obraz. Wektor cech obrazu jest wykorzystywany jako wejście modelu
językowego, który przewiduje kolejne słowa opisu w sposób sekwencyjny. Dzięki temu możliwe
jest automatyczne tworzenie zdań opisujących zawartość sceny, obecne obiekty oraz relacje mię-
dzy nimi. Model został wytrenowany na dużych zbiorach zawierających obrazy wraz z opisami
tekstowymi, co pozwoliło mu nauczyć się powiązań między reprezentacją wizualną a językiem
naturalnym. Podejście to zapoczątkowało intensywny rozwój metod multimodalnych łączących
analizę obrazu i przetwarzanie języka naturalnego. Zadanie generowania opisów obrazów jest
szczególnie wymagające, ponieważ wymaga zarówno rozpoznania obiektów, jak i zrozumienia ich
kontekstu. Analiza tego modelu pozwala zrozumieć sposób integracji reprezentacji wizualnych z
modelami sekwencyjnymi oraz podstawy współczesnych systemów multimodalnych.

## Praca nad projektem

_Jeśli chcesz tylko uruchomić projekt przejdź do sekcji [Uruchomienie projektu](#uruchomienie-projektu)._

Do łatwego zainstalowania używanych narzędzi CLI został wykorzystany program [mise](https://mise.jdx.dev/).

1. Zainstaluj `mise` zgodnie z [instrukcjami](https://mise.jdx.dev/getting-started.html).
2. Zainstaluj narzędzia CLI, uruchamiając `mise install`.
3. Opcjonalnie skonfiguruj automatyczne dodanie narzędzi zainstalowanych przez `mise` do PATH zgodnie z [instrukcją](https://mise.jdx.dev/getting-started.html#activate-mise).
4. Zainstaluj zależności łącznie z deweloperskimi `uv sync --all-extras`.
4.1. Jeżeli masz kartę graficzną serii RTX 50xx, zainstaluj odpowiednią wersję PyTorch: `uv pip install --force-reinstall --pre torch torchvision torchaudio --index-url https://download.pytorch.org/whl/nightly/cu128`
5. Zainstaluj hooki git uruchamiając `lefthook install`.

## Uruchomienie projektu

Do zarządzania wersją python oraz pakietami użyte zostało narzędzie [uv](https://docs.astral.sh/uv/). Jest napisane w Rust i jest znacznie szybsze od pozostałych opcji 😎

1. Zainstaluj `uv` zgodnie z [instrukcjami na stronie projektu](https://docs.astral.sh/uv/getting-started/installation/) (jeśli nie zainstalowałeś go wcześnie za pomocą `mise`).
2. Uruchom `uv sync` w katalogu projektu, aby zainstalować zależności i utworzyć środowisko wirtualne.
3. Jeżeli masz kartę graficzną serii RTX 50xx, zainstaluj odpowiednią wersję PyTorch: `uv pip install --force-reinstall --pre torch torchvision torchaudio --index-url https://download.pytorch.org/whl/nightly/cu128`
4. Pobierz [wagi modelu](https://drive.google.com/open?id=189VY65I_n4RTpQnmLGj7IzVnOF6dmePC) do katalogu `checkpoints/`, jeśli nie chcesz samodzielnie trenować modelu.
5. Pobierz i rozpakuj przygotowane dane [treningowe](http://images.cocodataset.org/zips/train2014.zip) i [testowe](http://images.cocodataset.org/zips/val2014.zip) do katalogu `dataset/`.
6. Uruchom `uv run create_input_files.py` żeby wygenerować dane wejściowe dla modelu na podstawie pobranych danych.
7. Uruchom wybrany Jupyter Notebook korzystając z wirtualnego środowiska python jako kernela.

## Eksperyment ze słownikiem

Aby porównać wpływ `min_word_freq` na jakość opisów, wygeneruj osobne zbiory danych dla kilku progów:

```bash
python create_input_files.py --min-word-freq 10
python create_input_files.py --min-word-freq 50
python create_input_files.py --min-word-freq 100
```

Następnie wytrenuj osobny model dla każdej wersji danych, podając zgodny `--data-name` w `train.py` i `eval.py`, np. dla `min_word_freq=10`:

```bash
python train.py --data-name coco_5_cap_per_img_10_min_word_freq
python eval.py --data-name coco_5_cap_per_img_10_min_word_freq --checkpoint PATH_TO_CHECKPOINT --word-map-file PATH_TO_WORDMAP
```

Analogicznie wykonaj trening i ewaluację dla `50` oraz `100`.
