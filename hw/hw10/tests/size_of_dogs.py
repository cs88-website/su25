test = {
  'name': 'size_of_dogs',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> SELECT name FROM size_of_dogs WHERE size="toy" OR size="mini";
          ace
          ellie
          finn
          ginger
          hank
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'ordered': False,
      'scored': True,
      'setup': r"""
      sqlite> .read hw06.sql
      """,
      'teardown': '',
      'type': 'sqlite'
    }
  ]
}
