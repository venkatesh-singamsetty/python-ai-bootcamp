- https://colab.research.google.com/drive/1iIGpaD_Jlshf0Ojto8rF9HsfNqSkjNme#scrollTo=mBhfNQNGmF9Y
- https://huggingface.co/settings/tokens - venky-huggingface
- https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0
- https://huggingface.co/stabilityai/stable-audio-open-small
- https://huggingface.co/Wan-AI/Wan2.1-T2V-1.3B-Diffusers
- https://huggingface.co/docs/hub/index

```python
# Example of deleting a large variable and forcing garbage collection
import gc

# Assuming 'output' is a large variable from previous operations
# if 'output' in locals():
#     del output

# If you have other large variables, delete them here, e.g.:
# if 'some_other_large_df' in locals():
#     del some_other_large_df

# Force garbage collection
gc.collect()

print("Garbage collection initiated. If you had large variables, their memory should now be freed.")
```
