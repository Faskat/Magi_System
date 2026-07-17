# Magi_System

**faskat_navi** — личный хаб проектов в стиле Serial Experiments Lain.
Проекты показаны как «слои» (layers) с живыми превью сайтов, CRT-эффектами и
boot-последовательностью подключения к Вайрду. Английский по умолчанию,
кнопка `[en/ru]` переключает язык.

Весь сайт — один файл `index.html` без сборки и фреймворков.

## Локальный запуск

Любой статик-сервер, например:

```bash
python -m http.server 8123
# или
npm install && npm start
```

На `localhost` карточки Hidden Liders и Bunny_part автоматически цепляются к
локальным dev-серверам (`:3000` и `:8877`) и показывают живые превью.

## Живые превью (UPLINKS)

В конце `index.html` есть конфиг:

```js
var UPLINK_CONF = {
  hidden_liders: { pub: "", local: "http://localhost:3000" },
  bunny_part:    { pub: "", local: "http://localhost:8877" }
};
```

Впиши в `pub` публичные URL деплоев — и превью заработают для всех посетителей:
уменьшенный живой iframe на карточке, клик — разворот на весь экран.
Пустой `pub` = заглушка «awaiting uplink».

## Деплой на Railway

1. New Service → GitHub Repo → `Faskat/Magi_System` (Root Directory не нужен).
2. `railway.json` уже задаёт сборку и старт (`serve` на `$PORT`).
3. Settings → Networking → Generate Domain.

## Слои

| Layer | Проект        | Статус                          |
|-------|---------------|---------------------------------|
| 01    | Hidden Liders | online, live preview            |
| 02    | lainwave      | classified                      |
| 03    | Reisync       | live demo (тема EVA-08)         |
| 04    | Bunny_part    | classified, live preview        |
| 05    | WorldEditor   | field test, локальная сборка    |
| 06    | —             | no carrier (зарезервировано)    |
