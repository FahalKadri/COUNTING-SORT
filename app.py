from flask import Flask, render_template, request

app = Flask(__name__)

def counting_sort_with_steps(arr):
    steps = []

    steps.append(f"Step 1: Input Data: {arr}")

    if not arr:
        return [], steps

    max_val = max(arr)
    min_val = min(arr)
    range_val = max_val - min_val + 1

    steps.append(
        f"Step 2: Find range: Max={max_val}, Min={min_val}. Range needed: {range_val}"
    )

    count = [0] * range_val
    steps.append(
        f"Step 3: Initialize Count Array of size {range_val} with 0s: {count}"
    )

    for num in arr:
        count[num - min_val] += 1
    steps.append(f"Step 4: Frequencies counted: {count}")

    for i in range(1, len(count)):
        count[i] += count[i - 1]
    steps.append(f"Step 5: Cumulative counts (used to find positions): {count}")

    output = [0] * len(arr)
    for num in reversed(arr):
        output[count[num - min_val] - 1] = num
        count[num - min_val] -= 1

    steps.append("Step 6: Output array constructed by placing elements in correct positions.")
    steps.append(f"Step 7: Final Sorted Result: {output}")

    return output, steps

@app.route("/", methods=["GET", "POST"])
def index():
    steps = []
    sorted_output = []

    if request.method == "POST":
        input_numbers = request.form["numbers"]
        arr = list(map(int, input_numbers.split(",")))
        sorted_output, steps = counting_sort_with_steps(arr)

    return render_template("index.html", steps=steps, sorted_output=sorted_output)

if __name__ == "__main__":
    app.run(debug=True)
