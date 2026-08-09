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

## Деплой

Сайт — статика, поэтому сервер ему не нужен: держать ради него включённый
контейнер незачем.

### GitHub Pages (по умолчанию)

`.github/workflows/pages.yml` при каждом пуше в `main` собирает `_site` из
`index.html` и `favicon.svg` и публикует его. Один раз нужно включить:
Settings → Pages → Source → **GitHub Actions**. Адрес будет
`https://faskat.github.io/Magi_System/`, свой домен подключается там же.

### Cloudflare Pages / Vercel (альтернатива)

Подключить репозиторий, build command оставить пустым, output directory — корень
(`.`). Конфиги не нужны.

### Railway (старый вариант)

`railway.json` и зависимость `serve` остались для совместимости: пока Pages не
включён, сервис на Railway продолжает работать. После переезда сервис можно
удалить, а вместе с ним — `railway.json` и `package.json`.

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
