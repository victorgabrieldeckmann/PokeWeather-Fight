# Entrar na pasta do projeto
cd SEU_REPOSITORIO

# Instalar suporte para ambiente virtual Python
sudo apt install python3.14-venv -y

# Criar ambiente virtual
python3 -m venv venv

# Ativar ambiente virtual
source venv/bin/activate

# Instalar dependências
pip install flask

# Iniciar aplicação
python app.py