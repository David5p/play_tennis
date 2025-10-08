document.addEventListener("DOMContentLoaded", function () {
  const startSelect = document.getElementById("id_start_time");
  const endSelect = document.getElementById("id_end_time");

  if (startSelect && endSelect) {
    startSelect.addEventListener("change", function () {
      const startIndex = startSelect.selectedIndex;
      if (startIndex >= 0 && startIndex < endSelect.options.length - 1) {
        endSelect.selectedIndex = startIndex + 1;
      }
    });
  }
});
