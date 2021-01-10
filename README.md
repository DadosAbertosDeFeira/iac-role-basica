# IaC

Esse repositório por hora servirá de espaço para organização do time de infra para o projeto Dados Abertos De Feira.

Aqui teremos a lista de tarefas e qualquer documento necessário pra ajudar pessoas a começarem a ajudar.

## Desenvolvimento:

### Requisitos:

 - Instale o [Python 3](https://www.python.org/downloads/)
 - Instale o [Molecule](https://molecule.readthedocs.io/en/latest/installation.html):

    ```
    $ python3 -m venv .venv
    $ source .venv/bin/activate
    $ pip install "molecule[docker,lint]" pytest-testinfra
    ```

 - Testando a role:

    ```
    $ molecule test
    ```

 - Testando rapidamente após modificação:

   ```
    $ molecule create
    $ molecule converge
    $ molecule verify
   ```

 - Não esqueça de destruir quando acabar seus testes:

    ```
    $ molecule destroy
    ```
