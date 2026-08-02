# Magi_System

**Faskat** — личный сайт-визитка: короткое описание, список проектов строками
и контакты. Тёмная тема по умолчанию, светлая и русский — кнопками в футере.
Фон — разреженная решётка моноширинных глифов на `<canvas>`: часть символов
подмигивает сама, всё вокруг курсора подсвечивается.

Весь сайт — один файл `index.html` без сборки и фреймворков.

## Локальный запуск

Любой статик-сервер, например:

```bash
python -m http.server 8123
```

или

```bash
npm install && npm start
```

## Деплой на Railway

1. New Service → GitHub Repo → `Faskat/Magi_System` (Root Directory не нужен).
2. `railway.json` уже задаёт сборку и старт (`serve` на `$PORT`).
3. Settings → Networking → Generate Domain.

## Проекты в списке

| Проект        | Ссылка                                                | Статус   |
|---------------|-------------------------------------------------------|----------|
| Hidden Liders | skillful-amazement-production-4d2a.up.railway.app      | live     |
| lainwave      | web-production-19abe.up.railway.app                    | live     |
| Bunny_part    | bunnypart-production.up.railway.app                    | live     |
| Reisync       | github.com/Faskat/Reisync                              | github   |
| Terraformer   | —                                                      | local    |

Тексты дублируются атрибутами `data-en` / `data-ru` — чтобы добавить проект,
достаточно скопировать строку `.row` в блоке `Projects`.
