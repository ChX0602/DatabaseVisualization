# Flexible database query service.

## Sample queries


1. This query returns the educational institutions of members of first 5 companies that receives series-b funding.
`query {
  allFundingRounds(fundingRoundType:"series-b", first:5){
    edges {
      node {
        object {
          RNemployees {
            edges {
              node {
                personObject {
                  RNeducation {
                    edges {
                      node {
                        institution
                      }
                    }
                  }
                }
              }
            }
          }
        }
      }
    }
  }
}
`
And the result will be of the following format:
`
{
  "data": {
    "allFundingRounds": {
      "edges": [
        {
          "node": {
            "object": {
              "RNemployees": {
                "edges": [
                  {
                    "node": {
                      "personObject": {
                        "RNeducation": {
                          "edges": [
                            {
                              "node": {
                                "institution": "Boston University"
                              }
                            }
                          ]
                        }
                      }
                    }
                  },
                  {
                    "node": {
                      "personObject": {
                        "RNeducation": {
                          "edges": [
                            {
                              "node": {
                                "institution": "Saint Mary's (Canada)"
                              }
                            },
                            {
                              "node": {
                                "institution": "Dalhousie (Canada)"
                                .
                                .
                                .
`

