Sub Stock_Total()

Dim Summary_Row_Counter As Integer
Dim Stk_Name As String 'Card_Name
Dim Vol_Total As Double 'Card_Total
Dim i As Long
Summary_Row_Counter = 2

'find the last row
lastrownumber = ActiveSheet.Cells(Rows.Count, "A").End(xlUp).Row
'MsgBox (lastrownumber)
Range("j1").Value = "Stock Ticker"
Range("K1").Value = "Total Volume"
'Range(K2:K").Format = Number

    For i = 2 To lastrownumber

    If Range("A" & i + 1) <> Range("A" & i) Then

        Vol_Total = Vol_Total + Range("G" & i).Value


        Stk_Name = Range("A" & i).Value


        Range("J" & Summary_Row_Counter).Value = Stk_Name

        Range("K" & Summary_Row_Counter).Value = Vol_Total

        Summary_Row_Counter = Summary_Row_Counter + 1

        Vol_Total = 0

    Else

        Vol_Total = Vol_Total + Range("G" & i).Value
    End If

    Next i

End Sub