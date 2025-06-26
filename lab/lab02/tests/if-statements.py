test = {
  'name': 'What If?',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> def ab(c, d):
          ...     if c > 5:
          ...         print(c)
          ...     elif c > 7:
          ...         print(d)
          ...     print('foo')
          >>> ab(10, 20)
          9b344c1a3735ca700721d36878fb0341
          42081a6c404d36ad9a5b11cd1b16ae28
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> def bake(cake, make):
          ...    if cake == 0:
          ...        cake = cake + 1
          ...        print(cake)
          ...    if cake == 1:
          ...        print(make)
          ...    else:
          ...        return cake
          ...    return make
          >>> bake(0, 29)
          cf2e1ad2c681425ba709dfa2ee9bde0f
          16ccc232210151f94dd8f231dfd218c0
          16ccc232210151f94dd8f231dfd218c0
          # locked
          >>> bake(1, "mashed potatoes")
          fb1fc60806a369f958fadcff081f616a
          d4c995d32aeaeba23839e9430fbed1ab
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
