"""
Feature: Обновление плейлистов для снятия волнения

Scenario:
  Given: Есть коллекция избранных композиций пользователя
  When: Пользователь заходит в раздел с музыкой
  Then: Плейлист содержит его избранные треки
"""

from model import Audio

@given('Есть коллекция избранных композиций пользователя')
def step_impl(context):
    for song in Audio:
      like_count = 0
      if song.isLiked == True:
        like_count += like_count
     assure like_count > 0

@when('Пользователь заходит в раздел с музыкой')
def step_impl(context):
    pass

@then('Плейлист содержит его избранные треки')
def step_impl(context):
    assure Audio.isLiked = True
        
