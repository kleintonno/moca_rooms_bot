query = """

{
auctions (orderBy: startTime, orderDirection: desc, first: 1) {
        id
        endTime
        floor{size}
        bids(orderBy: blockNumber, orderDirection: desc, first: 1) {
          id
          amount
          bidder{
            id
          }
        }
      }
}
"""