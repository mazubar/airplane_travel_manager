Feature: Рекомендации по эмоциональному состоянию

Scenario: Пользователь отмечает негативные эмоции
  Given пользователю предлагается отметить состояние
  When пользователь отмечает, что он нервничает / боится
  Then появляются информационные карточки с успокаивающими установками и советами
  And предлагаются медитации
  And предлагаются плейлисты с успокаивающей музыкой
