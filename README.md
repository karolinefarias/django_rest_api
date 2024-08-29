# Django REST API - Gerenciamento de Tarefas

Este é um projeto simples de uma API RESTful para gerenciamento de tarefas, desenvolvido usando Django e Django REST Framework.

## Funcionalidades

- **Visualizar Tarefas**: Obtenha uma lista de todas as tarefas ou busque por tarefas com base em parâmetros específicos.
- **Adicionar Tarefas**: Crie uma nova tarefa.
- **Atualizar Tarefas**: Atualize uma tarefa existente com base em seu ID.
- **Excluir Tarefas**: Exclua uma tarefa existente com base em seu ID.

## Endpoints da API

Abaixo estão os endpoints disponíveis na API:

- **Visualizar todas as tarefas**:  
  `GET /all`

- **Buscar tarefas por título**:  
  `GET /?titulo=titulo_name`

- **Buscar tarefas por data de criação**:  
  `GET /?data_criacao=yyyy-mm-dd`

- **Adicionar uma nova tarefa**:  
  `POST /create`

- **Atualizar uma tarefa existente**:  
  `PUT /update/pk`

- **Excluir uma tarefa existente**:  
  `DELETE /delete/pk`

## Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/nome-do-repositorio.git
   ```

2. Navegue até o diretório do projeto:
   ```bash
   cd nome-do-repositorio
   ```

3. Crie e ative um ambiente virtual:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # No Windows use `venv\Scripts\activate`
   ```

4. Instale as dependências necessárias:
   ```bash
   pip install -r requirements.txt
   ```

5. Execute as migrações do banco de dados:
   ```bash
   python manage.py migrate
   ```

6. Inicie o servidor de desenvolvimento:
   ```bash
   python manage.py runserver
   ```

7. Acesse a API através de `http://127.0.0.1:8000/`.

## Como Usar

- Para visualizar todas as tarefas, faça uma requisição `GET` para `/all`.
- Para buscar uma tarefa por título ou data de criação, faça uma requisição `GET` para o endpoint base com os parâmetros `titulo` ou `data_criacao`.
- Para adicionar uma nova tarefa, faça uma requisição `POST` para `/create` com os dados da tarefa no corpo da requisição.
- Para atualizar uma tarefa existente, faça uma requisição `PUT` para `/update/pk` substituindo `pk` pelo ID da tarefa a ser atualizada.
- Para excluir uma tarefa, faça uma requisição `DELETE` para `/tarefa/pk/delete`, substituindo `pk` pelo ID da tarefa a ser excluída.

## Estrutura do Projeto

- **models.py**: Define o modelo de dados `Tarefa`.
- **serializers.py**: Define o serializador `TarefaSerializer` para o modelo `Tarefa`.
- **views.py**: Contém as funções da API para manipular as tarefas (CRUD).

## Requisitos

- Python 3.10
- Django
- Django REST Framework

## Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

---

Você pode personalizar o conteúdo acima conforme necessário para se adequar melhor ao seu projeto.
