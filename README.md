# Introduction-to-Statistical-Modeling-for-Data-Analysis-with-Python

## 環境構築

### 1. Pipenvによる構築

```bash
pip install pipenv
pipenv install
pipenv shell
```

### 2. Dockerによる構築

```bash
$docker build ./ -t <image_name>
$docker run -it --name <container_name> <image_name> /bin/bash
```

## 動作環境(2021.8.6時点)

- cycler==0.10.0
- kiwisolver==1.3.1
- matplotlib==3.4.2
- numpy==1.21.1
- pandas==1.3.1
- Pillow==8.3.1
- pyparsing==2.4.7
- python-dateutil==2.8.2
- pytz==2021.1
- rdata==0.5
- six==1.16.0
- xarray==0.19.0
