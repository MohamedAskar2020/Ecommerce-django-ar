<div class="my-3 p-3 bg-white rounded shadow-sm">
    <h6 class="border-bottom border-gray pb-2 mb-0">التعليقات</h6>
    {% for comment in comments %}
    <div class="media text-muted pt-3">
      <svg class="bd-placeholder-img mr-2 rounded" width="32" height="32" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Placeholder: 32x32" preserveAspectRatio="xMidYMid slice" focusable="false"><title>Placeholder</title><rect width="100%" height="100%" fill="#007bff"/><text x="50%" y="50%" fill="#007bff" dy=".3em">32x32</text></svg>
        
      <p class="media-body pb-3 mb-0 small lh-125 border-bottom border-gray">
        <strong class="d-block text-gray-dark">{{comment.name}} في {{comment.comment_date|date'd-m-Y'}}</strong>
            {{comment.body}}
      </p>
    </div>
    {% endfor %}
    <small class="d-block text-right mt-3">
      <a href="#">كل التعليقات</a>
    </small>
</div>
