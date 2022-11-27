# Cloud-Project

* João Vitor Magalhães

Esse projeto tem como objetivo criar uma aplicação que seja user friendly, de forma que é possível provisionar uma infraestrutura na AWS através do terminal.
Nessa aplicação será possível construir, alterar e deletar recursos na AWS.

## Tutorial de Instalação e Operação da aplicação

Primeiro de tudo é nescessário fazer a instalação do Terraform

No link a seguir é possível seguir um tutorial de como instalar o Terraform no seu Sistema Operacional.
[Terraform](https://developer.hashicorp.com/terraform/downloads).

Para finalmente podermos usar o Terraform, basta configurar a AWS. Faremos isso com a AWS CLI.

A partir desse link você pode baixar a AWS CLI. [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html).

Para terminar as configurações segue o link: [Interface da Linha de Comando da AWS](https://aws.amazon.com/pt/cli/)

Nesse passo você deve inserir suas IAM credentials (Access Key e Secret Access Key) para autenticar o Terraform AWS provider. **Não torne essas credenciais públicas de forma alguma!!!**

## Executando aplicação

Por fim, será necessário executar a aplicação.
Primeiro, abra seu terminal e entre no diretório que seu arquivo se encontra e então rode a seguinte linha de comando:

```
python main.py
```

Isso irá fazer com que apareça no seu terminal uma série de possíveis ações que você pode tomar a seguir.

    1. Criar instância
    - É possível criar uma instânica escolhendo o nome e o tipo. Ademais, você pode associá-la ou não a um Security Group existente.
    2. Criar VPC
    - É possível criar uma VPC através do nome, criando também uma subnet e um gateway.
    3. Criar usuário
    - É possível criar um usuário escolhendo o nome.
    4. Criar Security Group
    - É possível criar um Security Group escolhendo o nome.
    5. Destruir instância
    - Lista as instâncias e permite com que seja deletada pelo nome.
    6. Deletar usuário
    - Lista os usuários e permite com que seja deletado pelo nome.
    7. Destruir Security Group
    - Lista os Security Groups existentes e permite com que seja deletado pelo nome.
    8. Listar instâncias
    - Lista as instâncias e suas regiões, os usuários, os grupos de segurança e as VPCs.
    9. Destruir tudo
    - Deleta tudo o que foi criado com terraform destroy.
    0. Sair
    - Encerra a aplicação.