filtersClear = document.querySelector(".filter-clear");
allFilter = document.querySelector(".all-filter");
filter = document.URL.split("=")[1];
postFilter = document.querySelector(".post-filter");
commentFilter = document.querySelector(".comment-filter");
replyFilter = document.querySelector(".reply-filter");
if (!filter) {
  allFilter.classList.add("selected");
  filtersClear.classList.add("d-none");
} else if (filter == "Comment") {
  commentFilter.classList.add("selected");
} else if (filter == "Post") {
  postFilter.classList.add("selected");
} else if (filter == "Reply") {
  replyFilter.classList.add("selected");
}

selectedElement = document.querySelector(".selected");
filters = document.querySelectorAll(".filter li a");
for (i = 0; i < filters.length; i++) {
  filters[i].onclick = toggleSelection;
};

allFilteranchor = document.querySelector(".all-filter a");
filtersClear.onclick=function(){
  // selectedElement.classList.toggle("selected");
  // allFilter.classList.toggle("selected");
  // filtersClear.classList.add("d-none");
  allFilteranchor.click();
};

function toggleSelection() {
  selectedElement.classList.toggle("selected");
  this.parentElement.classList.toggle("selected");
  if(((selectedElement==allFilter)&&(this.parentElement!=allFilter))||((selectedElement!=allFilter)&&(this.parentElement==allFilter))){
   filtersClear.classList.toggle("d-none");
  }
  
  selectedElement = this.parentElement;
};
