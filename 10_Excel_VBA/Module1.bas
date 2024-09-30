Attribute VB_Name = "Module1"
Sub variousScripts()

    ' Create variables to hold winners. (Use "Long" because the numbers exceed the limit for integers)
    Dim first_place As Long
    Dim second_place As Integer
    Dim firstname As String
    Dim ingredients(5) As String
    Dim runnerUp2 As Double

    ingredients(0) = "peanut_butter"

    second_place = 2
    Total = (second_place * (1 + second_place) * second_place)

    MsgBox (ingredients(0))
    MsgBox (Total)
    MsgBox ("Hello World")

    ' ----------------------------------------

    ' Inserting Data Via Cells
    Cells(2, 1).Value = "Cat"
    Cells(2, 2).Value = "In"
    Cells(2, 3).Value = "The"
    Cells(2, 4).Value = "Hat"

    ' Inserting Data Via Ranges
    Range("F1").Value = "I"
    Range("F2").Value = "Am"
    Range("F3").Value = "Sam"

    ' Inserting Data Across Ranges
    Range("F5:F7") = 5
    
    ' Bringing cell data from the Spreadsheet into a Variable here in the backend
    Dim mybucket As Integer
    mybucket = Cells(1, 1).Value
    MsgBox (mybucket)

    ' ----------------------------------------

    ' Basic String Variable

    Dim name As String
    name = "Gandalf"

    Dim title As String
    title = "The Great"

    Dim fullname As String
    fullname = name + " " + title

    MsgBox (fullname)

    MsgBox ("I am " + Str(second_place) + " years old.")
    MsgBox ("I am " & age1 & " years old.") ' Notice either way works but must use either + or & but not both

    ' ------------------------------------------
    
    ' String Splitting Example
 
    Dim words() As String
    Dim Shakespeare As String
    Shakespeare = "To be or not to be. That is the question"
    words = Split(Shakespeare, " ")
    MsgBox (words(0))

    ' ------------------------------------------

    
    ' Simple Conditional Example
    
    If Range("A2").Value > Range("B2").Value Then
        MsgBox ("Num 1 is greater than Num 2")
    End If

    ' Simple Conditional with If, Else, and Elseif
    ' ------------------------------------------
    If Range("A5").Value > Range("B5").Value Then
        MsgBox ("Num 3 is greater than Num 4")

    ElseIf Range("A5").Value < Range("B5").Value Then
        MsgBox ("Num 4 is greater than Num 3")

    Else
        MsgBox ("Num 3 and Num 4 are equal")

    End If

    ' Conditional with Operators (And)
    ' ------------------------------------------
    If (Range("A8").Value > Range("C8").Value And Range("B8").Value > Range("C8").Value) Then
        MsgBox ("Both Num 5 and Num 6 are greater than Num 7")
    End If

    ' Conditional with Operators (OR)
    ' ------------------------------------------
    If (Range("A8").Value > Range("C8").Value Or Range("B8").Value > Range("C8").Value) Then
        MsgBox ("Either Num 5 and/or Num 6 is greater than Num 7")
    End If


    ' ------------------------------------------
    ' set the Font color to Red
    Range("A1").Font.ColorIndex = 3
    ' set the background color to Red
    Range("A2:A5").Interior.ColorIindex = 3


    ' ------------------------------------------

    Dim LastRow As String
    LastRow = ws.Cells(Rows.Count, 1).End(xlUp).Row






    ' Loop through each of the lotto tickets
    For i = 1 To 1001

        ' Check if the lotto number matches the first place winner...
        If Cells(i, 3).Value = first_place Then

            ' If so, create a message box specifying the first place win
            MsgBox " Congratulations " + Cells(i, 1).Value

            ' Retrieve the values associated with the winner and enter them into the winner's box.
            Cells(2, 6).Value = Cells(i, 1).Value
            Cells(2, 7).Value = Cells(i, 2).Value
            Cells(2, 8).Value = first_place

        ' Check if the lotto number matches the second place winner...
        ElseIf Cells(i, 3).Value = second_place Then
            
            ' Retrieve the values associated with the winner and enter them into the winner's box.
            Cells(3, 6).Value = Cells(i, 1).Value
            Cells(3, 7).Value = Cells(i, 2).Value
            Cells(3, 8).Value = second_place

        ' Check if the lotto number matches the second place winner...
        ElseIf Cells(i, 3).Value = third_place Then
           
            ' Retrieve the values associated with the winner and enter them into the winner's box.
            Cells(4, 6).Value = Cells(i, 1).Value
            Cells(4, 7).Value = Cells(i, 2).Value
            Cells(4, 8).Value = third_place

        ' Ends this series of IF/ELSE conditionals
        End If

    Next i

    ' Loop through the lotto tickets a second time to find the first instance of a "runner-up" winner

    For i = 1 To 1001

        ' BONUS: Check for runner ups with an OR operator
        If Cells(i, 3).Value = runner1 Or Cells(i, 3).Value = runner2 Or Cells(i, 3).Value = runner3 Then
            
            ' Retrieve the values associated with the winner and enter them into the winner's box.
            runner_up = Cells(i, 3).Value
            Cells(5, 6).Value = Cells(i, 1).Value
            Cells(5, 7).Value = Cells(i, 2).Value
            Cells(5, 8).Value = runner_up

            ' If first match is found, exit the for loop
            Exit For

        End If

    Next i

End Sub





' Looping through all of the Worksheets in an Excel File
Dim ws As Worksheet

For Each ws In Worksheets
    'do something here


















