from rest_framework import serializers
from .models import Director, Movie, Review



class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = 'name'. split()
#       fields = 'name'. split()юю

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['text', 'stars']

class MovieSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True)
    director = DirectorSerializer()
    ave_rating = serializers.SerializerMethodField()
    class Meta:
        model = Movie
        fields = ['title', 'description', 'duration', 'director', 'reviews', 'ave_rating']
        
    def get_ave_rating(self, movie):
        reviews_1 = movie.reviews.all()
        if reviews_1:
            sum_reviews = sum(i.stars for i in reviews_1)
            average = sum_reviews / len(reviews_1)
            return round(average, 1)
        return None



class DirectorValidateSerializer(serializers.Serializer):
    name = serializers.CharField()

class MoviesValidateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    description = serializers.CharField()
    duration = serializers.DurationField()
    director = serializers.BooleanField()
    reviews = serializers.ListField()
    ave_rating = serializers.IntegerField(min_value=1, max_value=10000)

class ReviewsValidateSerializer(serializers.Serializer):
    text = serializers.CharField(required=False, default='N22t')
    stars = serializers.FloatField(default=0)