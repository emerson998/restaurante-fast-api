# 🍽️ API de Gerenciamento de Restaurantes

Esta é uma **API robusta** para gerenciamento de restaurantes, desenvolvida em **Python** utilizando o *framework* **FastAPI**.

A aplicação permite a gestão completa de restaurantes e seus respectivos pratos, oferecendo funcionalidades como:
* Criação e listagem de restaurantes.
* Adição e listagem de pratos em um restaurante específico.

## 📐 Arquitetura

A aplicação foi estruturada seguindo os princípios de **Clean Architecture**, promovendo a separação de preocupações, testabilidade e manutenibilidade. A estrutura de camadas é a seguinte:

$$\text{API} \rightarrow \text{Use Case} \rightarrow \text{Repository} \rightarrow \text{Database}$$

| Camada | Responsabilidade |
| :--- | :--- |
| **API** | Define as rotas HTTP e lida com a requisição/resposta. |
| **Use Case** | Contém as regras de negócio e orquestra as operações. |
| **Repository** | Define a interface para acesso a dados (abstração do banco). |
| **Database** | Implementa a persistência de dados (e.g., SQLAlchemy). |

## 🚀 Requisitos

Para rodar a aplicação, você precisará ter instalado:

* **Python 3.10** ou superior
* **pip** (gerenciador de pacotes Python)
* **Git** (opcional, para clonar o repositório)

## 📁 Estrutura do Projeto

A organização do código segue o padrão de Clean Architecture:

---

## ⚙️ Como Rodar a Aplicação

Siga os passos abaixo para ter a API rodando em sua máquina local.
python -m venv venv

## Para Windows
venv\Scripts\activate

## Para Linux / Mac
source venv/bin/activate

## Instale os pacotes necessários para a aplicação:
pip install fastapi uvicorn sqlalchemy

## Rodar a API
uvicorn app.main:app --reload

A API estará disponível em: http://127.0.0.1:8000
Você pode acessar a documentação interativa (Swagger UI) em: http://127.0.0.1:8000/docs

## Instalar Dependências de Teste
pip install pytest pytest-asyncio httpx coverage

## Rodar Testes
pytest -v

## Executa os testes e coleta os dados de cobertura
coverage run -m pytest

## Gera o relatório no terminal
coverage report -m

## Gera um relatório HTML interativo
coverage html

## Abrir o relatório HTML (Exemplo para Windows)
start htmlcov/index.html

