<!DOCTYPE html>
<html>
<head>
<title>Special Day</title>

<script>

function specialday(m1,d1,m2,d2)

{
if (m1<m2)

{
document.write("After current day")
}

else if (m2<m1)

{
document.write("Before current day")
}

else if (d1<d2)

{
document.write("After current day")
}

else if (d2<d1)

{
document.write("Before current day")
}

else
{
document.write("Special day")
}

}
specialday(2,15,2,15)

</script>

</body>
</html>
</head>
