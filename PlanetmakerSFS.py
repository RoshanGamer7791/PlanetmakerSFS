import json
import math
import os
import tkinter as tk
from tkinter import ttk, filedialog

print("Planet maker script")
print("By ilikespace and Roshan The Modder\n")
print("")
print("End result should be in this folder\n")

root = tk.Tk()
root.geometry("0x0")

def get_user_input(prompt, default_value):
    user_input = input(f"{prompt} (default {default_value}): ")
    return float(user_input) if user_input else default_value


def get_color_input(prompt, default_value):
    user_input = input(f"{prompt} (default r,g,b,a): ")
    if user_input:
        r, g, b, a = map(float, user_input.split(","))
        return {"r": r, "g": g, "b": b, "a": a}
    return {
        "r": default_value[0],
        "g": default_value[1],
        "b": default_value[2],
        "a": default_value[3],
    }


def generate_config():
    # Base Data
    print("Base Data configs\n")
    radius = get_user_input("Enter radius", 314970.0)
    gravity = get_user_input("Enter gravity", 9.8)
    timewarpHeight = get_user_input("Enter timewarp height", 25000)
    velocityArrowsHeight = get_user_input("Enter velocity arrows height", 5000)
    map_color = get_color_input("Enter map color (RGBA (Red Green Blue Alpha))", (0.45, 0.68, 1.0, 1.0))
    print("")
    
    # Actual Atmosphere data
    print("Atmosphic Physics data configs\n")
    actual_atmo = get_user_input("Enter actual atmosphere height", 30000.0)
    density = get_user_input("Enter atmosphere density", 0.005)
    curve = get_user_input("Enter Curve", 10.0)
    parachuteMultiplier = get_user_input("Enter Parachute Multiplier", 1.0)
    upperAtmosphere = get_user_input("Enter Upper Atmosphere multiplier", 0.333)
    shockwaveIntensity = get_user_input("Enter Shockwave Intensity", 1.0)
    minHeatingVelocityMultiplier = get_user_input("Enter Minimum Heating Velocity Multiplier", 1.0)
    print("")
    
    # Visual Atmosphere
    print("Atmospherice Visual data configs\n")
    positionZ = get_user_input("Enter PositionZ", 4000)
    visual_atmo = get_user_input("Enter visual atmosphere height", 45000.0)
    visual_atmo_tex = input("Enter Atmosphere gradient (default: Atmo_Earth") or "Atmo_Earth"
    print("")
    
    # Cloud Data
    print("Cloud configs\n")
    cloud_tex = input("Enter Cloud Texture (Default: Earth_Clouds)") or "Earth_Clouds"
    cloud_start_height = get_user_input("Enter cloud start height", 1200)
    cloud_height = get_user_input("Enter cloud height", 36000.0)
    circumference = 2 * math.pi * radius
    cloud_alpha = get_user_input("Enter cloud alpha", 0.1)
    cloud_velocity = get_user_input("Enter cloud velocity", 2.0)
    print("")
    
    # Front Cloud Data
    print("Front Cloud Configs\n")
    frontclouds_tex = input("Enter Front Clouds Texture (Default: Earth_Clouds_Front)") or "Earth_Clouds_Front"
    frontclouds_texcutout = get_user_input("Enter Front Clouds Texture cutout", 1.0)
    frontclouds_fadeZoneHeight = get_user_input("Enter Front Clouds Appearence height", 20000.0)
    frontclouds_height = get_user_input("Enter Front Clouds height", 10000.0)
    frontclouds_positionZ = get_user_input("Enter Front Clouds PostionZ", -5000.0)
    print("")
    
    # Rings Data
    print("Rings Configs\n")
    ringsTex = input("Enter Rings Texture (Default: Saturn_Rings)") or "Saturn_Rings"
    ringsStartRadius = get_user_input("Enter Rings Start Radius", 380000.0)
    ringsEndRadius = get_user_input("Enter Rings End Radius", 6600000.0)
    ringsPositionZ = get_user_input("Enter Rings Position Z", 5000.0)
    ringsMapColor = get_color_input("Enter Rings Map Color (RGBA (Red Green Blue Alpha))", (0.85, 0.75, 0.65, 0.2))
    print("")

    # Terrain Data
    print("Terrain data configs\n")
    planetTex = input("Input Planet Texture (Default: Earth_WithOceans)") or "Earth_WithOceans"
    planetTexCutout = get_user_input("Input Planet Texture Cutout", 0.9947)
    planetTexRotation = get_user_input("Input Planet Texture Rotation", 1.85)
    surfacelayersize = get_user_input("Input Surface Layer Size", 20)
    minFade = get_user_input("Input Minimun Fade", 0.0)
    MaxFade = get_user_input("Input Maximum Fade", 1.0)
    terrain_height_1 = get_user_input("Enter Terrain height 1", 35)
    terrain_height_2 = get_user_input("Enter Terrain height 2", 5)
    terrain_height_3 = get_user_input("Enter Terrain height 3", 1)
    print("")
    
    # Water Data
    print("Water Configs\n")
    OceanMaskTex = input("Input Ocean Mask Texture (default: Earth_OceansMaskV2)") or "Earth_OceansMaskV2"
    OceanDepth = get_user_input("Input Ocean Depth", 5000.0)
    OceanSandColor = get_color_input("Input Ocean Sand Color", (0.9, 0.86, 0.81, 1.0))
    OceanFloorColor = get_color_input("Input Ocean Floor Color", (0.25, 0.25, 0.25, 1.0))
    OceanShallowColor = get_color_input("Input Shallow Ocean Color", (0.1, 0.68, 1.0, 0.4))
    OceanDeepColor = get_color_input("Input Deep Ocean Color", (0.1, 0.15, 0.55, 1.0))
    waterGradientWidthMultipler = get_user_input("Input Water Gradient Multiplier", 0.5)
    sandGradientWidthMultipler = get_user_input("Input Sand Gradient Width Multipler", 2.0)
    floorGradientWidthMultipler = get_user_input("Input Floor Gradient Width Multiplier", 10.0)
    opacitySurface = get_user_input("Input Opacity Surface", 0.8)
    opactiyFar = get_user_input("Input Opacity Far", 1.0)
    opacityFullDarkness = get_user_input("Input Opacity Full Darkness", 0.95)
    surfaceVisibilityDistance = get_user_input("Input Full Surface Visibility Distance", 1200.0)
    fullDarknessDepth = get_user_input("Input Full Darkness Depth", 500.0)
    fullDarknessDepthVisibilityDistance = get_user_input("Input Full Darkness Depth Visibility Depth", 300.0)
    WaterMapColor = get_color_input("Input Water Map Color", (0.1, 0.4, 1.0, 0.4))
    print("")
    
    # Orbital Data
    print("Orbital Data configs\n")
    parent = input("Enter orbit parent (default Sun): ") or "Sun"
    semi_major_axis = get_user_input("Enter semi-major axis", 7480000000.0)
    eccentricity = get_user_input("Input Eccentricity", 0.0)
    argumentofperiapsis = get_user_input("Input Argument of Periapsis", 0.0)
    multipliersoi = get_user_input("Input Multiplier SOI", 2.5)
    print("")

    config_data = {
        "version": "1.5",
        "BASE_DATA": {
            "radius": radius,
            "radiusDifficultyScale": {},
            "gravity": gravity,
            "gravityDifficultyScale": {},
            "timewarpHeight": timewarpHeight,
            "velocityArrowsHeight": velocityArrowsHeight,
            "mapColor": map_color,
            "significant": True,
            "rotateCamera": True,
        },
        "ATMOSPHERE_PHYSICS_DATA": {
            "height": actual_atmo,
            "density": density,
            "curve": curve,
            "curveScale": {},
            "parachuteMultiplier": parachuteMultiplier,
            "upperAtmosphere": upperAtmosphere,
            "heightDifficultyScale": {},
            "shockwaveIntensity": shockwaveIntensity,
            "minHeatingVelocityMultiplier": minHeatingVelocityMultiplier,
        },
        "ATMOSPHERE_VISUALS_DATA": {
            "GRADIENT": {
                 "positionZ": positionZ, 
                 "height": visual_atmo, 
                 "texture": visual_atmo_tex
            },
            "CLOUDS": {
                "texture": cloud_tex,
                "startHeight": cloud_start_height,
                "width": circumference,
                "height": cloud_height,
                "alpha": cloud_alpha,
                "velocity": cloud_velocity,
            },
            "FOG": {
                "keys": []
            },
        },
        "FRONT_CLOUDS_DATA": {
            "cloudsTexture": frontclouds_tex,
            "cloudTextureCutout": frontclouds_texcutout,
            "fadeZoneHeight": frontclouds_fadeZoneHeight,
            "height": frontclouds_height,
            "positionZ": frontclouds_positionZ,
            "sharpenAlpha": True,
        },
        "RINGS_DATA": {
            "ringsTexture": ringsTex,
            "startRadius": ringsStartRadius,
            "endRadius": ringsEndRadius,
            "positionZ": ringsPositionZ,
            "mapColor": ringsMapColor
        },
        "TERRAIN_DATA": {
            "TERRAIN_TEXTURE_DATA": {
                "planetTexture": planetTex,
                "planetTextureCutout": planetTexCutout,
                "planetTextureRotation": planetTexRotation,
                "planetTextureDontDistort": True,
                "surfaceTexture_A": "Blured02",
                "surfaceTextureSize_A": {
                    "x": 20.0, 
                    "y": 8.0
                },
                "surfaceTexture_B": "None",
                "surfaceTextureSize_B": {
                    "x": -1.0, 
                    "y": -1.0
                },
                "terrainTexture_C": "Neutral",
                "terrainTextureSize_C": {
                    "x": 100.0, 
                    "y": 30.0
                },
                "surfaceLayerSize": surfacelayersize,
                "minFade": minFade,
                "maxFade": MaxFade,
                "shadowIntensity": 6.0,
                "shadowHeight": 15.0,
            },
            "terrainFormulaDifficulties": {
                "Normal": [
                    f"OUTPUT = AddHeightMap(Perlin,{circumference}, {terrain_height_1})",
                    f"OUTPUT = AddHeightMap(Perlin,{circumference}, {terrain_height_2})",
                    f"OUTPUT = AddHeightMap(Perlin,{circumference}, {terrain_height_3})",
                    "OUTPUT = Add(30)",
                ]
            },
            "textureFormula": [],
            "verticeSize": 2.0,
            "collider": True,
            "flatZones": [],
            "flatZonesDifficulties": {},
        },
        "WATER_DATA": {
            "oceanMaskTexture": OceanMaskTex,
            "lowerTerrain": True,
            "oceanDepth": OceanDepth,
            "sand": OceanSandColor,
            "floor": OceanFloorColor,
            "shallow": OceanShallowColor,
            "deep": OceanDeepColor,
            "maskGradient_Water": {"must": 1000.0, "cannot": 700.0, "global": 2000.0},
            "waterGradientWidthMultiplier": waterGradientWidthMultipler,
            "maskGradient_Terrain": {"must": 25.0, "cannot": 25.0, "global": 50.0},
            "sandGradientWidthMultiplier": sandGradientWidthMultipler,
            "floorGradientWidthMultiplier": floorGradientWidthMultipler,
            "shoreNoiseSize": {"x": 3000.0, "y": 1000.0},
            "sandNoiseSize": {"x": 500.0, "y": 100.0},
            "wavesSize": {"x": 16.0, "y": 0.3},
            "opacity_Surface": opacitySurface,
            "opacity_Far": opactiyFar,
            "opacity_FullDarkness": opacityFullDarkness,
            "surfaceVisibilityDistance": surfaceVisibilityDistance,
            "fullDarknessDepth": fullDarknessDepth,
            "fullDarknessVisibilityDistance": fullDarknessDepthVisibilityDistance,
            "mapColor": WaterMapColor,
        },
        "ORBIT_DATA": {
            "parent": parent,
            "semiMajorAxis": semi_major_axis,
            "smaDifficultyScale": {},
            "eccentricity": eccentricity,
            "argumentOfPeriapsis": argumentofperiapsis,
            "direction": 1,
            "multiplierSOI": multipliersoi,
            "soiDifficultyScale": {},
        },
        "ACHIEVEMENT_DATA": {
            "Landed": False,
            "Takeoff": True,
            "Atmosphere": True,
            "Orbit": True,
            "Crash": True,
        },
        "LANDMARKS": [],
    }

    return config_data


def write_config_to_file(config_data):
    root.withdraw()
    filename = filedialog.asksaveasfile(
        title="Save Planet Files",
        filetypes=[("SFS Planet Files", "*.txt")]
    )

    if not filename:
        return
    
    with open(filename, "w") as file:
        json.dump(config_data, file, indent=2)

    print(f"Saved to {filename}")


if __name__ == "__main__":
    config = generate_config()
    write_config_to_file(config)

