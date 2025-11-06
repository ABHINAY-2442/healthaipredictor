
# Generate requirements.txt file
requirements = """streamlit==1.28.0
numpy==1.24.3
pandas==2.0.3
scikit-learn==1.3.0
pickle-mixin==1.0.2
"""

with open('requirements.txt', 'w') as f:
    f.write(requirements)

print("✅ requirements.txt generated successfully!")
print("\nRequired packages:")
print(requirements)
