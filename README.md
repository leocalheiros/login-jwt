# Sistema de Autenticação JWT com Flask

Este é um projeto simples de autenticação via JWT (JSON Web Tokens) em uma API Flask. O projeto demonstra a autenticação JWT básica com algumas verificações. Não há integração com um banco de dados neste exemplo, pois o foco principal é mostrar como a autenticação JWT funciona.

## Funcionalidades

O projeto possui três rotas principais:

1. Rota `/auth` (Autenticação - POST):
   - Esta rota permite que um usuário obtenha um token JWT válido.
   - Um token é gerado com base em um UID (User ID) fictício para fins de demonstração.
   - O token é retornado como resposta da solicitação.

2. Rota `/secret` (Rota Secreta - GET):
   - Esta é uma rota protegida por autenticação JWT.
   - Somente usuários autenticados com um token válido podem acessar esta rota.
   - Se um usuário tentar acessar sem um token válido, receberá uma mensagem de erro.
   - Se um usuário autenticado acessar com um token válido, receberá uma mensagem secreta.

## Estrutura do Projeto

- `src/auth_jwt/token_handler/token_creator.py`: Classe para criar tokens JWT com base em um UID.
- `src/auth_jwt/token_handler/token_singleton.py`: Singleton que inicializa o `TokenCreator` com configurações do JWT.
- `src/auth_jwt/token_handler/token_verifier.py`: Função de decoração para verificar e autenticar tokens JWT em rotas protegidas.
- `src/auth_jwt/config/jwt_config_file.py`: Arquivo de configuração para armazenar as configurações do JWT.

## Configuração

As configurações do JWT, como a chave secreta e os tempos de expiração, são armazenadas em um arquivo `.env`. Certifique-se de criar um arquivo `.env` na raiz do projeto com as seguintes configurações:

```env
TOKEN_KEY=your_secret_key_here
EXP_TIME_MIN=60
REFRESH_TIME_MIN=30
```
- `TOKEN_KEY`: A chave secreta usada para assinar e verificar tokens JWT.
- `EXP_TIME_MIN`: O tempo de expiração dos tokens em minutos.
- `REFRESH_TIME_MIN`: O tempo mínimo restante antes da expiração para um token ser renovado automaticamente.

## Clone o repositório
```
git clone https://github.com/leocalheiros/login-jwt.git
```

## Acesse o diretório do projeto
```
cd login-jwt
```

## Instale as dependências
```
pip install -r requirements.txt
```

## Inicie o servidor
```
python run.py
```
