# Plate_Layout

Short code to automate the random layout of 24-well plates for C. elegans feeding assays. Because the position of the well on the 24-well plate can affect the reading, putting the different strains in random locations can prevent counfounding variables. For example, all of the wells on the sides of the plate can dry out faster, altering the height of the agar and thus the fluorescence reading. Generates a csv file:

Example
+---------+---------+---------+---------+----+---------+
| Plate 1 |         |         |         |    |         |
+---------+---------+---------+---------+----+---------+
| C       | C       | C       | C       | C  | CX16904 |
+---------+---------+---------+---------+----+---------+
| CX16904 | C       | CX12311 | CX16904 | N2 | CX12311 |
+---------+---------+---------+---------+----+---------+
| N2      | C       | CX12311 | CX16904 | N2 | CX12311 |
+---------+---------+---------+---------+----+---------+
| CX16904 | CX16904 | CX16904 | N2      | N2 | CX16904 |
+---------+---------+---------+---------+----+---------+

Uses random, time, and argparse
