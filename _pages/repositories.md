---
layout: article
title: Repositories
show_title: false
---

<style>
.repo-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 1rem;
  margin-top: 1rem;
}
</style>

**Repositories**

{% if site.data.repositories.github_repos %}
<div class="repo-grid">
  {% for repo in site.data.repositories.github_repos %}
    {% include repository/repo.html repository=repo %}
  {% endfor %}
</div>
{% endif %}
