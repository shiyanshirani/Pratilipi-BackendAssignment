from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=250, blank=True, null=False)
    story = models.TextField(blank=True, null=False)
    date_published = models.DateTimeField(auto_now_add=True)
    user_id = models.CharField(max_length=120, blank=True, null=False)
    read_count = models.PositiveIntegerField(default=0, blank=False)
    like_count = models.PositiveIntegerField(default=0, null=False)

    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"

    def __str__(self):
        return "{0} - {1}".format(self.user_id, self.title)

    def get_input_filename(self):
        if self.csv_file:
            filename = str(self.input_file.name).split("/")
            return filename[-1]
        else:
            return None

    def get_input_file(self):
        if self.csv_file:
            return self.csv_file.url
        else:
            return None
