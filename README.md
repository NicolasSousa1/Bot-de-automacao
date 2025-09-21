# 🛠️ Automação de Cadastro de Produtos

- Este projeto é um **script em Python** que automatiza o cadastro de produtos em um sistema web. Ele utiliza **PyAutoGUI** para controlar o navegador e **Pandas** para ler os dados de um arquivo CSV com os produtos.

- O objetivo é agilizar processos repetitivos, economizando tempo e evitando erros manuais.

---

## 🔹 Funcionalidades

- Abrir o navegador Google Chrome automaticamente.
- Acessar o sistema via link.
- Fazer login automático com e-mail e senha.
- Ler dados de um CSV (`produtos.csv`) contendo:
  - Código do produto
  - Marca
  - Tipo
  - Categoria
  - Preço unitário
  - Custo
  - Observações (opcional)
- Preencher o formulário do sistema e cadastrar múltiplos produtos automaticamente.

---

## ⚙️ Pré-requisitos

- Python 3.x instalado  
- Google Chrome instalado  
- Bibliotecas Python:

- Pyautogui
- Pandas 
- Time


## 🚀 Como executar
- Abra o script automacao_cadastro.py.

- Verifique se o CSV produtos.csv contém os produtos que deseja cadastrar.

- Ajuste as coordenadas de clique do PyAutoGUI caso necessário (dependendo da resolução da tela).

- Execute o script:

- O script abrirá o Chrome, fará login e cadastrará automaticamente todos os produtos listados no CSV.

## ⚙️ Descobrindo coordenadas do mouse

- O projeto inclui o arquivo pegar_posição.py, que serve para descobrir as coordenadas do mouse em seu computador. Isso é útil caso seja necessário ajustar os cliques do PyAutoGUI devido a diferentes resoluções de monitor.

- Para usar:

- Abra o terminal e execute:

- python pegar_posição.py


- O script aguardará 5 segundos antes de começar.

- Mova o mouse até o ponto desejado na tela.

- As coordenadas do mouse serão exibidas no terminal.

- Use essas coordenadas para atualizar os cliques no script principal (automacao_cadastro.py).

- O script também realiza um pequeno scroll de 200 pixels para facilitar testes de posições.

## ⚠️ Observações importantes

- O script utiliza coordenadas de clique fixas, então ele funciona melhor em telas com resolução constante.



