from django.shortcuts import render
from .forms import BitwiseForm
from .models import Bitwise

# Create your views here.

def operations(request):  # Renamed from bitwise_view
    result = None
    if request.method == 'POST':
        form = BitwiseForm(request.POST)
        if form.is_valid():
            values = [form.cleaned_data[f] for f in ['a', 'b', 'c', 'd', 'e']]
            warnings = []

            if any(v < 0 for v in values):
                warnings.append("Warning: Negative values detected.")

            average = sum(values) / len(values)                
            if average > 50:
                warnings.append("Note: Average is greater than 50.")
            count_positive = len([v for v in values if v > 0])
            even_odd = ["even" if int(v) & 1 == 0 else "odd" for v in values]
            sorted_over_10 = sorted([v for v in values if v > 10])

            # Save to MongoDB using Django model
            bitwise_record = Bitwise.objects.create(
                original=values,
                sorted_over_10=sorted_over_10,
                average=average,
                count_positive=count_positive,
                even_odd=even_odd,
                warnings=warnings
            )

            result = {
                "original": bitwise_record.original,
                "sorted_over_10": bitwise_record.sorted_over_10,
                "average": bitwise_record.average,
                "count_positive": bitwise_record.count_positive,
                "even_odd": bitwise_record.even_odd,
                "warnings": bitwise_record.warnings
            }
    else:
        form = BitwiseForm()

    return render(request, 'bitwise/results.html', {'form': form, 'result': result})