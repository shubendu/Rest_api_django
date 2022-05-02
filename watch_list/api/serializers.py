from rest_framework import serializers
from watch_list.models import WatchList, StreamPlatform, Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"

class WatchListSerializer(serializers.ModelSerializer): # USING ModelSerializer
    #len_name = serializers.SerializerMethodField()  # ADding custom serializer field
    reviews = ReviewSerializer(many = True, read_only = True)

    class Meta:
        model = WatchList
        fields = "__all__" # It'll will show all the fields
        #fields = ['id','name','description'] #You can choose your fields accordingly
        #exclude = ['active'] #What if you want all the fields but not the one then you can exclude that one field
    

class StreamPlatformSerializer(serializers.ModelSerializer):
    watchlist = WatchListSerializer(many = True, read_only = True)
    # watchlist = serializers.StringRelatedField(many = True) #You'll get only name
    # watchlist = serializers.PrimaryKeyRelatedField(many = True, read_only = True) #You'll get only Primary Key
    # watchlist = serializers.HyperlinkedRelatedField(many = True, read_only = True, view_name='movie-detail')


    class Meta:
        model = StreamPlatform
        fields = "__all__"

    # def get_len_name(self, object):
    #     return len(object.name)

    # def validate(self, data):  #Object-level Validation
    #     if data['name'] == data['description']:
    #         raise serializers.ValidationError("Title and Description should be different!")
    #     else:
    #         return data

    # def validate_name(self, value): #Field-level Validation
    #     if len(value)<2:
    #         raise serializers.ValidationError("Name is too short!")
    #     else:
    #         return value




# def name_length(value):
#     if len(value)<2:
#         raise serializers.ValidationError("Name is too short!")
#     return value

# class MovieSerializer(serializers.Serializer):  #CUSING Serializer
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[name_length])
#     description = serializers.CharField()
#     active = serializers.BooleanField()

#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance

#     def validate(self, data):  #Object-level Validation
#         if data['name'] == data['description']:
#             raise serializers.ValidationError("Title and Description should be different!")
#         else:
#             return data

    # def validate_name(self, value): #Field-level Validation
    #     if len(value)<2:
    #         raise serializers.ValidationError("Name is too short!")
    #     else:
    #         return value
