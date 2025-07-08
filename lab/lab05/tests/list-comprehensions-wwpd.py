test = {
  'name': 'Comprehensions',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> [2 * x for x in range(4)]
          8ad525f5463563c8e2eb1b70e75f3010
          # locked
          >>> [y for y in [6, 1, 6, 1] if y > 2]
          814e6f716d7c11a58da15edcbd06ebdf
          # locked
          >>> [[1] + s for s in [[4], [5, 6]]]
          0625a32f5dbc5c688e7a3006a866b1ae
          # locked
          >>> [z + 1 for z in range(10) if z % 3 == 0]
          8ec4477f46e13692676c53fdb20fabf2
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
