# Multiples of Y And X

Skriptiä ja testejä voi ajaa joko koneelle asennetulla Python 2.7 tulkilla tai
käyttäen Docker ohjelmaa, jos sellainen koneelta löytyy.

## Skriptin suoritus

```bash
python multples_of_y_and_x.py input.txt output.txt
```

## Robot testien käynnistys

```bash
# Tulokset tallentuvat results alihakemistoon
./runtests.sh
```

## Suoritus Docker containerissa

### Imagen luonti

```bash
docker build -t multiples .
```

### Skriptin suoritus

```bash
docker run -it --rm --name multiples -v "$PWD/results":/usr/src/app/results multiples
```

### Robot testit

```bash
# Tulokset tallentuvat (isäntä koneen) results alihakemistoon
docker run -it --rm --name multiples -v "$PWD/results":/usr/src/app/results multiples robot
```
