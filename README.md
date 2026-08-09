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

### Railway (боевой)

1. New Service → GitHub Repo → `Faskat/Magi_System` (Root Directory не нужен).
2. `railway.json` задаёт сборку и старт (`serve` на `$PORT`), автодеплой при пуше.
3. Settings → Networking → Generate Domain.

### Serverless (наготове, не включён)

Сайт — чистая статика: ни бэкенда, ни запросов к своему серверу, все ссылки
внешние, `favicon.svg` относительный, так что подкаталог тоже подходит. Переезд
на бесплатный CDN без единой правки кода:

- **GitHub Pages** — `.github/workflows/pages.yml` уже лежит в репозитории и
  собирает `_site` из `index.html` и `favicon.svg`. Запускается только вручную,
  чтобы не мешать Railway. Чтобы включить: Settings → Pages → Source →
  **GitHub Actions**, затем Actions → *Deploy to GitHub Pages* → Run workflow.
  Адрес — `https://faskat.github.io/Magi_System/`. Если Pages станет основным
  хостом, вернуть в workflow триггер `push`.
- **Cloudflare Pages / Vercel** — подключить репозиторий, build command пустой,
  output directory — корень (`.`). Конфиги не нужны.

После переезда (если он случится) `railway.json`, `package.json` и зависимость
`serve` больше не нужны — они только для контейнера.

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
