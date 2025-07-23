
# Calculadora GUI com PySide6 🖥️🧮

Projeto de uma calculadora com interface gráfica desenvolvida em Python, utilizando a biblioteca PySide6 (Qt para Python). A aplicação oferece operações matemáticas básicas, interface responsiva e tratamento de erros.

---

## Funcionalidades Principais ✨

- Interface gráfica moderna com PySide6
- Campo de exibição interativo para entrada de números e operadores
- Exibição de informações e expressões em construção
- Botões funcionais para operações aritméticas, potência, inversão de sinal, limpar e apagar
- Tratamento de erros (divisão por zero, overflow) com mensagens de alerta ⚠️
- Uso de sinais e slots para interação entre componentes 🔄

---

## Estrutura do Projeto 📂

```
calculadora/
│
├── main.py          # Arquivo principal para execução da aplicação
├── display.py       # Componentes Display e Info (exibição e informações)
├── buttons.py       # Layout e funcionalidades dos botões da calculadora
├── style.py         # Configuração do tema visual da aplicação
├── window.py        # Implementação da janela principal da interface
├── utilities.py     # Funções auxiliares para validação e conversão numérica
├── icon.ico         # Ícone da aplicação
```

---

## Como Executar 🚀

1. Clone o repositório:

```bash
git clone https://github.com/deboracmg/calculadora.git
```

2. (Opcional) Crie e ative um ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate     # Linux/Mac
venv\Scripts\activate.bat  # Windows
```

3. Instale a dependência necessária:

```bash
pip install PySide6
```

4. Execute a aplicação:

```bash
python main.py
```

---

## Tecnologias 🛠️

- Python 3.7+
- PySide6 (Qt para Python)

---

## Licença 📄

Este projeto está licenciado sob a **MIT License**.  
Veja o arquivo [LICENSE](LICENSE) para detalhes.

---



Desenvolvido por [@deboracmg](https://github.com/deboracmg)  
