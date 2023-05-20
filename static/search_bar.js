// Функция для обработки нажатия клавиши Enter
function handleKeyPress(event) {
    if (event.keyCode === 13) { // Код клавиши Enter
      handleSearch();
    }
  }
  
  // Функция для выполнения поиска
  function handleSearch() {
    const inputElement = document.getElementById('filter-input');
    handleFilterChange(inputElement);
    updateQuestionCount(); // Обновляем значение question.count
  }
  
  // Функция для обработки изменений в фильтре
  function handleFilterChange(inputElement) {
    const filterValue = inputElement.value.trim().toLowerCase();
    const questionTitles = document.querySelectorAll('.question-title');
    questionTitles.forEach(function(title) {
      const questionTitleText = title.textContent.toLowerCase();
      if (questionTitleText.includes(filterValue)) {
        title.parentNode.style.display = 'block';
      } else {
        title.parentNode.style.display = 'none';
      }
    });
  }
  
  // Функция для обновления значения question.count
  function updateQuestionCount() {
    const questionCountElement = document.getElementById('question-count');
    const visibleQuestions = document.querySelectorAll('.question-title');
    const count = Array.from(visibleQuestions).filter(function(title) {
      return title.parentNode.style.display !== 'none';
    }).length;
    questionCountElement.textContent = 'Total number of questions: ' + count;
  }
  
  // Назначение обработчика события для поля ввода
  const inputElement = document.getElementById('filter-input');
  inputElement.addEventListener('keypress', handleKeyPress);  