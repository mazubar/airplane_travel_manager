Feature: Внесение информации о предстоящем рейсе

Scenario Outline: Незаполненные обязательные поля
   Given: Пользователь заполняет поля <number>, <departure>
   When: Пользователь нажимает кнопку "сохранить"
   Then: Система выдает предупреждение о том, что не все обязательные поля заполнены
   And: Незаполненные обязательные поля выделяются красным цветом
  
Scenario Outline: Успешное сохранение
     Given: Пользователь заполняет поля <number>, <departure>
     When: пользователь нажимает кнопку "сохранить"
     Then: появляется окно, сообщающее, что информация сохранена
     And: в соответствующем разделе появляется состояние рейса
     And: предлагается настроить уведомления об изменении состояния рейса
     
Examples: Success
     | number    | departure        |
     | 220A      | 21/11/06 16:30   |  
     

Examples: Fail     
     | 107B      | NULL             |
     | NULL      | 21/11/06 16:30   |
