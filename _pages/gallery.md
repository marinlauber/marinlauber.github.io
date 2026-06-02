---
layout: article
title: Gallery
show_title: false
---

<style>
.gallery-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
  gap: 1.5rem;
  margin-top: 1rem;
}

.gallery-card {
  background: #fff;
  border: 1px solid #e8e8e8;
  border-radius: 6px;
  overflow: hidden;
  box-shadow: 0 1px 4px rgba(0,0,0,0.06);
  display: flex;
  flex-direction: column;
  cursor: pointer;
  transition: box-shadow 0.2s, transform 0.2s;
}

.gallery-card:hover {
  box-shadow: 0 4px 16px rgba(0,0,0,0.13);
  transform: translateY(-2px);
}

.gallery-card__media {
  position: relative;
  width: 100%;
  aspect-ratio: 16 / 9;
  overflow: hidden;
  background: #111;
}

.gallery-card__media img {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

/* Play button overlay for video/youtube cards */
.gallery-card__play {
  position: absolute;
  inset: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  background: rgba(0,0,0,0.28);
  transition: background 0.2s;
}

.gallery-card:hover .gallery-card__play {
  background: rgba(0,0,0,0.42);
}

.gallery-card__play svg {
  width: 48px;
  height: 48px;
  filter: drop-shadow(0 2px 6px rgba(0,0,0,0.5));
}

.gallery-card__body {
  padding: 0.85rem 1rem;
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 0.3rem;
}

.gallery-card__title {
  font-size: 0.9rem;
  font-weight: 600;
  color: #333;
  margin: 0;
}

.gallery-card__caption {
  font-size: 0.82rem;
  color: #555;
  line-height: 1.5;
  margin: 0;
}

/* Modal */
.gallery-modal {
  display: none;
  position: fixed;
  inset: 0;
  background: rgba(0,0,0,0.88);
  z-index: 9999;
  align-items: center;
  justify-content: center;
  padding: 1.5rem;
}

.gallery-modal.is-open {
  display: flex;
}

.gallery-modal__inner {
  position: relative;
  width: 100%;
  max-width: 1000px;
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}

.gallery-modal__media {
  position: relative;
  width: 100%;
  aspect-ratio: 16 / 9;
  background: #000;
  border-radius: 4px;
  overflow: hidden;
}

.gallery-modal__media img,
.gallery-modal__media video,
.gallery-modal__media iframe {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: contain;
  border: none;
}

.gallery-modal__caption {
  color: #ddd;
  font-size: 0.85rem;
  line-height: 1.6;
  text-align: center;
}

.gallery-modal__caption a {
  color: #aaa;
  text-decoration: underline;
}

.gallery-modal__close {
  position: absolute;
  top: -2.5rem;
  right: 0;
  background: none;
  border: none;
  color: #fff;
  font-size: 2rem;
  line-height: 1;
  cursor: pointer;
  padding: 0 0.25rem;
  opacity: 0.8;
}

.gallery-modal__close:hover {
  opacity: 1;
}
</style>

**Gallery**

<div class="gallery-grid">
  {% for item in site.data.gallery %}
  {% if item.youtube %}
    {% assign media_type = "youtube" %}
    {% assign media_src  = item.youtube %}
    {% assign thumb_src  = "https://img.youtube.com/vi/" | append: item.youtube | append: "/hqdefault.jpg" %}
  {% elsif item.src contains '.mp4' or item.src contains '.webm' %}
    {% assign media_type = "video" %}
    {% assign media_src  = item.src %}
    {% assign thumb_src  = "" %}
  {% else %}
    {% assign media_type = "image" %}
    {% assign media_src  = item.src %}
    {% assign thumb_src  = item.src %}
  {% endif %}

  <div class="gallery-card"
       data-type="{{ media_type }}"
       data-src="{{ media_src }}"
       data-caption="{{ item.caption | markdownify | strip_html | escape }}"
       data-caption-html="{{ item.caption | markdownify | escape }}">
    <div class="gallery-card__media">
      {% if media_type == "youtube" %}
      <img src="{{ thumb_src }}" alt="{{ item.title }}" loading="lazy">
      {% elsif media_type == "video" %}
      <video muted playsinline preload="metadata" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover;">
        <source src="{{ media_src }}#t=0.5" type="video/{{ item.src | split: '.' | last }}">
      </video>
      {% else %}
      <img src="{{ thumb_src }}" alt="{{ item.title | default: item.caption }}" loading="lazy">
      {% endif %}
      {% if media_type == "youtube" or media_type == "video" %}
      <div class="gallery-card__play">
        <svg viewBox="0 0 80 80" fill="none" xmlns="http://www.w3.org/2000/svg">
          <circle cx="40" cy="40" r="38" fill="rgba(0,0,0,0.55)" stroke="white" stroke-width="2"/>
          <polygon points="32,24 60,40 32,56" fill="white"/>
        </svg>
      </div>
      {% endif %}
    </div>
    <div class="gallery-card__body">
      {% if item.title %}<p class="gallery-card__title">{{ item.title }}</p>{% endif %}
      <div class="gallery-card__caption">{{ item.caption | markdownify }}</div>
    </div>
  </div>
  {% endfor %}
</div>

<!-- Lightbox modal -->
<div id="gallery-modal" class="gallery-modal" role="dialog" aria-modal="true" aria-label="Media viewer">
  <div class="gallery-modal__inner">
    <button class="gallery-modal__close" id="gallery-modal-close" aria-label="Close">&#x2715;</button>
    <div class="gallery-modal__media" id="gallery-modal-media"></div>
    <div class="gallery-modal__caption" id="gallery-modal-caption"></div>
  </div>
</div>

<script>
(function () {
  var modal      = document.getElementById('gallery-modal');
  var mediaEl    = document.getElementById('gallery-modal-media');
  var captionEl  = document.getElementById('gallery-modal-caption');

  function openModal(card) {
    var type    = card.dataset.type;
    var src     = card.dataset.src;
    var caption = card.dataset.captionHtml;

    if (type === 'youtube') {
      mediaEl.innerHTML = '<iframe src="https://www.youtube.com/embed/' + src +
        '?autoplay=1&rel=0" allow="autoplay; encrypted-media" allowfullscreen></iframe>';
    } else if (type === 'video') {
      mediaEl.innerHTML = '<video autoplay controls loop playsinline>' +
        '<source src="' + src + '" type="video/' + src.split('.').pop() + '">' +
        '</video>';
    } else {
      mediaEl.innerHTML = '<img src="' + src + '" alt="">';
    }

    captionEl.innerHTML = unescape(caption);
    modal.classList.add('is-open');
    document.body.style.overflow = 'hidden';
  }

  function closeModal() {
    mediaEl.innerHTML = '';
    captionEl.innerHTML = '';
    modal.classList.remove('is-open');
    document.body.style.overflow = '';
  }

  document.querySelectorAll('.gallery-card').forEach(function (card) {
    card.addEventListener('click', function () { openModal(card); });
  });

  document.getElementById('gallery-modal-close').addEventListener('click', function (e) {
    e.stopPropagation();
    closeModal();
  });

  modal.addEventListener('click', function (e) {
    if (e.target === modal) closeModal();
  });

  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') closeModal();
  });
})();
</script>
