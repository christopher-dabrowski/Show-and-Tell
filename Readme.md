# Show and Tell

[![Pylint](https://github.com/christopher-dabrowski/Show-and-Tell/actions/workflows/pylint.yml/badge.svg)](https://github.com/christopher-dabrowski/Show-and-Tell/actions/workflows/pylint.yml)

![Python Version from PEP 621 TOML](https://img.shields.io/python/required-version-toml?tomlFilePath=https%3A%2F%2Fraw.githubusercontent.com%2Fchristopher-dabrowski%2FShow-and-Tell%2Frefs%2Fheads%2Fmaster%2Fpyproject.toml&style=for-the-badge&logo=python)

Projekt akademicki, którego celem jest poznanie algorytmu Show and Tell.
Projekt bazuje na pracy [Show and Tell: A Neural Image Caption Generator](https://arxiv.org/pdf/1411.4555.pdf) oraz repozytorium [a-PyTorch-Tutorial-to-Image-Captioning](https://github.com/sgrvinod/a-PyTorch-Tutorial-to-Image-Captioning).

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

## Uruchomienie projektu

Do zarządzania wersją python oraz pakietami użyte zostało narzędzie [uv](https://docs.astral.sh/uv/). Jest napisane w Rust i jest znacznie szybsze od pozostałych opcji 😎

1. Zainstaluj `uv` zgodnie z [instrukcjami na stronie projektu](https://docs.astral.sh/uv/getting-started/installation/).
2. Uruchom `uv sync` w katalogu projektu, aby zainstalować zależności i utworzyć środowisko wirtualne.
