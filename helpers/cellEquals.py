def CellEquals(cell1, cell2):
    return cell1.isRevealed == cell2.isRevealed and cell1.isMine == cell2.isMine and cell1.neighborMinesCount == cell2.neighborMinesCount and cell1.clickCounter == cell2.clickCounter
