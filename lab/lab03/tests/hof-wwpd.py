test = {
  'name': 'Higher Order Functions',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # If Python displays <function...>, type Function, if it errors type Error, if it displays nothing type Nothing
          >>> def cake():
          ...    print('beets')
          ...    def pie():
          ...        print('sweets')
          ...        return 'cake'
          ...    return pie
          >>> chocolate = cake()
          e31a1314e797f365711f3a5a81edccb8
          # locked
          >>> chocolate
          409d225c8d71bdae383b166e754adf05
          # locked
          >>> chocolate()
          cd3d3af9ea482488c844d97463435760
          8bea18841ac0d9369fb59855e3f3b86d
          # locked
          >>> more_chocolate, more_cake = chocolate(), cake
          cd3d3af9ea482488c844d97463435760
          # locked
          >>> more_chocolate
          8bea18841ac0d9369fb59855e3f3b86d
          # locked
          >>> # Reminder: cake, more_cake, and chocolate were defined/assigned in the code above! 
          >>> # It might be helpful to refer to their definitions on the assignment website so you don't have to scroll as much!
          >>> def snake(x, y):
          ...    if cake == more_cake:
          ...        return chocolate
          ...    else:
          ...        return x + y
          >>> snake(10, 20)
          409d225c8d71bdae383b166e754adf05
          # locked
          >>> snake(10, 20)()
          cd3d3af9ea482488c844d97463435760
          8bea18841ac0d9369fb59855e3f3b86d
          # locked
          >>> cake = 'cake'
          >>> snake(10, 20)
          c53337f505de5cbe3d7ee515953b1526
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        }
      ],
      'scored': False,
      'type': 'wwpp'
    }
  ]
}
