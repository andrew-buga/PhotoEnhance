# 🎨 PhotoEnhance — AI Photo Upscaler

> Безкоштовне покращення якості фотографій за допомогою AI (Real-ESRGAN) через Google Colab.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/andrew-buga/PhotoEnhance/blob/main/PhotoEnhance_MVP.ipynb)

---

## ✨ Можливості

| Функція | Статус |
|---|---|
| ✅ Завантаження фото (JPG, PNG, WEBP) | MVP |
| ✅ Вибір масштабу: ×2, ×4, ×8 | MVP |
| ✅ AI обробка через Real-ESRGAN | MVP |
| ✅ Before/After порівняння | MVP |
| ✅ Скачування результату | MVP |
| ✅ Автозбереження у Google Drive | MVP |
| 🔜 Веб-інтерфейс (React) | v2 |
| 🔜 Batch обробка | v2 |
| 🔜 Видалення фону | v2 |

---

## 🚀 Швидкий старт (MVP — Google Colab)

### Крок 1 — Відкрий Notebook у Colab

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/andrew-buga/PhotoEnhance/blob/main/PhotoEnhance_MVP.ipynb)

Або вручну: [colab.research.google.com](https://colab.research.google.com) → File → Open Notebook → GitHub → вставити URL репозиторію.

### Крок 2 — Увімкни GPU

```
Runtime → Change runtime type → Hardware accelerator: T4 GPU → Save
```

### Крок 3 — Запускай клітинки по порядку

| Клітинка | Що робить | Запуск |
|---|---|---|
| **Cell 1** — Setup | Встановлює Real-ESRGAN та залежності | 1 раз |
| **Cell 2** — GPU Check | Перевіряє GPU (має бути T4) | 1 раз |
| **Cell 3** — Drive Mount | Підключає Google Drive | 1 раз |
| **Cell 4** — UI | Завантаження фото + вибір налаштувань | 1 раз |
| **Cell 5** — Process | AI обробка фото | Кожне фото |
| **Cell 6** — Preview | Before/After + скачування | Після обробки |

---

## 🤖 Доступні моделі

| Модель | Для чого | Розмір |
|---|---|---|
| `RealESRGAN_x4plus` | Загальні фото, реальні сцени | 67 MB |
| `RealESRGAN_x4plus_anime_6B` | Аніме та ілюстрації | 67 MB |
| `RealESRGAN_x2plus` | Менше збільшення, швидша обробка | 67 MB |
| `ESRGAN_SRx4_DF2KOST` | Старі / деградовані фото | 63 MB |

---

## 📊 Технічні вимоги

| Параметр | MVP (Colab) | v2 (Web) |
|---|---|---|
| Час обробки | 5–60 сек | 10–90 сек |
| Макс. розмір фото | 10 MB | 25 MB |
| Формати | JPG, PNG | JPG, PNG, WEBP, TIFF |
| GPU | T4 16GB (Colab) | RunPod Serverless |
| Вартість | **$0** | ~$5–20/міс |

---

## 🗺️ Дорожня карта

- [x] **Тиждень 1–2** — MVP: Google Colab Notebook із Real-ESRGAN + UI
- [ ] **Тиждень 3** — Проектування веб-інтерфейсу (Figma)
- [ ] **Тиждень 4–5** — React фронтенд + FastAPI бекенд
- [ ] **Тиждень 6** — Інтеграція RunPod Serverless
- [ ] **Тиждень 7–8** — Тестування, оптимізація, деплой на Vercel

---

## 🛠️ Стек технологій

### MVP
- **AI модель**: [Real-ESRGAN](https://github.com/xinntao/Real-ESRGAN) (open source, Xintao Wang)
- **GPU**: Google Colab T4 (безкоштовно)
- **UI**: Jupyter ipywidgets
- **Сховище**: Google Drive (15 GB безкоштовно)

### v2 (Веб-сайт)
- **Фронтенд**: React 18 + Tailwind CSS
- **Хостинг**: Vercel (безкоштовно)
- **Бекенд**: FastAPI (Python)
- **GPU**: RunPod Serverless (~$0.00025/сек)
- **Сховище**: Cloudflare R2 / AWS S3
- **БД**: Supabase (free tier)

---

## 🧪 Запуск локально (опціонально)

```bash
# Клонування
git clone https://github.com/andrew-buga/PhotoEnhance.git
cd PhotoEnhance

# Встановлення залежностей
pip install basicsr facexlib gfpgan realesrgan

# Запуск Jupyter
jupyter notebook PhotoEnhance_MVP.ipynb
```

> ⚠️ Для локального запуску потрібна NVIDIA GPU з мінімум 4 GB VRAM.

---

## 📁 Структура проекту

```
PhotoEnhance/
├── PhotoEnhance_MVP.ipynb   # 🎯 Google Colab Notebook (MVP)
├── README.md                # Документація
├── .gitignore
└── .github/
    └── ISSUE_TEMPLATE/      # Шаблони для issues
```

---

## ⚠️ Відомі обмеження

| Ризик | Вплив | Мітигація |
|---|---|---|
| Colab завершує сесію на великих фото | Середній | Обмеження: 10 MB, tile-режим |
| Google може обмежити безкоштовний GPU | Високий | Backup: Kaggle Notebooks |
| Real-ESRGAN погано на деяких типах фото | Низький | Декілька моделей на вибір |

---

## 📄 Ліцензія

MIT License — можна вільно використовувати, змінювати та розповсюджувати.

---

## 🙏 Подяки

- [Real-ESRGAN](https://github.com/xinntao/Real-ESRGAN) — Xintao Wang та команда
- [Google Colab](https://colab.research.google.com) — безкоштовні GPU
