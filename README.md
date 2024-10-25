# Microsoft Account Generator

Este é um projeto em Python que gera automaticamente contas da Microsoft para o usuário, com base em um arquivo `contas.txt`. O script lê o arquivo, processa as informações e exibe as contas geradas.

## Funcionalidades

- Leitura do arquivo `contas.txt` para usar como base de dados.
- Geração automática de contas da Microsoft.
- Exibição das contas geradas diretamente no terminal.

## Requisitos

- Python 3.x
- Um arquivo `contas.txt` contendo as informações das contas.

### Exemplo de `contas.txt`

O arquivo `contas.txt` deve seguir o seguinte formato:

```
email1@example.com:password1
email2@example.com:password2
email3@example.com:password3
```

Cada linha deve conter um e-mail e uma senha separados por dois pontos (`:`).

## Instalação

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/Gameriano1/contagenerator.git
   ```

2. **Acesse a pasta do projeto:**

   ```bash
   cd microsoft-account-generator
   ```

3. **Instale as dependências necessárias:**

   Se o projeto exigir bibliotecas adicionais, instale-as utilizando `pip`:

   ```bash
   pip install -r requirements.txt
   ```

## Como Usar

1. **Coloque o arquivo `contas.txt` na pasta do projeto.**

2. **Execute o script:**

   Execute o arquivo principal `gerador_contas.py` (ou outro nome que o script tenha) para iniciar o processo de geração de contas.

   ```bash
   python gerador_contas.py
   ```

3. **Visualize as contas geradas:**

   O script exibirá no terminal as contas que foram lidas e processadas a partir do arquivo `contas.txt`.

### Exemplo de Saída

Após rodar o script, você verá uma saída semelhante a esta no terminal:

```
Contas geradas com sucesso:
- email1@example.com:password1
- email2@example.com:password2
- email3@example.com:password3
```

## Contribuições

Contribuições são sempre bem-vindas! Sinta-se à vontade para abrir issues e pull requests para melhorias ou correções.

## Licença

Este projeto está licenciado sob a MIT License.

---

Desenvolvido por RAXY 2021.
