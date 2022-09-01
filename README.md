#  <p align="center">RISC-V Performance Measurement Tool</p>
![Cyclist](https://github.com/Zvorky/Cyclist/blob/main/artwork/cyclist_logo.svg)
### Português  
- Ferramenta em CLI (Interface de Linha de Comando) para cálculos de performance de programas em linguagem de máquina para a arquitetura [RISC-V](https://github.com/riscv).  
- [Esta ferramenta](https://github.com/Zvorky/Cyclist/blob/main/modules/CPI.py) calcula a quantidade total de ciclos gastos e média de [Ciclos Por Instrução (CPI)](https://pt.wikipedia.org/wiki/Ciclos_por_instru%C3%A7%C3%A3o) de um programa e auxilia com cálculos relacionados a tais informações.  
- Por hora, apenas a extensão [RV32I](https://five-embeddev.com/riscv-isa-manual/latest/rv32.html) é suportada.

### English
- CLI (Command Line Interface) performance measurement tool for machine language programs for [RISC-V](https://github.com/riscv) architecture.
- [This tool](https://github.com/Zvorky/Cyclist/blob/main/modules/CPI.py) calculates the total number of cycles and average [Cycles Per Instruction (CPI)](https://en.wikipedia.org/wiki/Cycles_per_instruction) of a program and helps with related calculations.
- By now, this supports [RV32I](https://five-embeddev.com/riscv-isa-manual/latest/rv32.html) only.

---
# <p align="center">Usage</p>
<p align="center"><img src=https://github.com/Zvorky/Cyclist/blob/main/artwork/Cyclist_Splash.png></p>

## Português
- Você pode executar a CLI completa rodando o [Cyclist.py](https://github.com/Zvorky/Cyclist/blob/main/Cyclist.py)
<p align="left">ou</p>

- Rodar apenas o módulo [CPI.py](https://github.com/Zvorky/Cyclist/blob/main/modules/CPI.py)  
  
### Selecionando Arquivo  
Insira "select" para acessar a página de seleção de arquivo, insira o caminho para seu arquivo em linguagem de máquina.  
### Calculando CPI
Insira "cpi" e receba seu relatório.  
  
## English
- You can run the complete CLI by launching [Cyclist.py](https://github.com/Zvorky/Cyclist/blob/main/Cyclist.py)
<p align="left">or</p>

- Run the [CPI.py](https://github.com/Zvorky/Cyclist/blob/main/modules/CPI.py) module only.

### Selecting File
Insert "select" to access the file selection page, insert the path to your machine language file.
### Calculating CPI
Insert "cpi" and get your report.
