# Configuração do Projeto

## Linux / Ubuntu

### Entrar na pasta do projeto

```bash
cd SEU_REPOSITORIO
```

### Instalar suporte para ambiente virtual Python

```bash
sudo apt update
sudo apt install python3.14-venv -y
```

### Criar ambiente virtual

```bash
python3 -m venv venv
```

### Ativar ambiente virtual

```bash
source venv/bin/activate
```

### Instalar dependências

```bash
pip install flask
```

### Iniciar aplicação

```bash
python app.py
```

---

## Windows (PowerShell)

### Entrar na pasta do projeto

```powershell
cd CAMINHO_DO_PROJETO
```

### Criar ambiente virtual

```powershell
python -m venv venv
```

### Ativar ambiente virtual

```powershell
.\venv\Scripts\Activate.ps1
```

> Caso apareça erro de permissão para executar scripts:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Depois tente ativar novamente:

```powershell
.\venv\Scripts\Activate.ps1
```

### Instalar dependências

```powershell
pip install flask
```

### Iniciar aplicação

```powershell
python app.py
```

---

## Verificar se o ambiente virtual está ativo

Se tudo estiver correto, o terminal exibirá algo parecido com:

```text
(venv) PS C:\projeto>
```

ou

```text
(venv) usuario@ubuntu:~/projeto$
```
