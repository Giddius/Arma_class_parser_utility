create table if not exists "image_blob_tbl" (
    "blob_id" integer primary key,
    "blob_name" text not null unique,
    "blob_data" blob unique
);
create table if not exists "cfgmods_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgexperience_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgaiskill_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgailevelpresets_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgdifficultypresets_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgdifficulties_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfginventory_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgcurator_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgsteamsettings_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgbrains_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgtexturetomaterial_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgmaterials_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgtlmaterials_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgvehicleactions_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgweaponcursors_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgminetriggers_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgammo_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgrecoils_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgmagazines_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfginventoryglobalvariable_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgdestroysounds_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgcloudlets_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgopticseffect_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgdestructpos_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgdamagearound_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfglights_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgcloth_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgvehicleclasses_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgfactionclasses_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgnonaivehicles_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgmarkedtargets_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgfsms_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgfatigue_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgfirstaid_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgdiving_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgbleeding_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgpriority_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgskeletonparameters_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgimprecision_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgbreathing_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgweaponhandling_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgpersonturret_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgmovesbasic_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfggesturesmale_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgslopelimits_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfganimation_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgcollisions_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgslingloading_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgvoice_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgvoicetypes_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgcoredata_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgvehicleicons_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgcloudletshapes_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgsavethumbnails_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgformations_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgwaypoints_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgragdollskeletons_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgvideooptions_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgsurfacecharacters_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgsurfaces_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgsoundenvirontocontrollers_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgdefaultsettings_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgpatches_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgfontfamilies_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgfonts_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgeditcamera_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgwrapperui_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgingameui_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfggroupicons_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgtasktypes_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgsimpletasks_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgdiary_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgactions_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgmissions_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgranks_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgdefaultkeyspresets_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgdetectors_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgfacewounds_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgglasses_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgfaces_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgmimics_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgenvsounds_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfghqidentities_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgheads_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgmusic_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgsounds_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgwhistlesound_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgtitles_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgintro_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgcredits_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgcutscenes_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgcameraeffects_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgmarkers_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgmarkercolors_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgmarkerbrushes_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfglocationtypes_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgworlds_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgworldlist_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfggroups_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgaddons_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgeditorobjects_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgmpgametypes_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfglivestats_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgachievements_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgvoicemask_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgrumble_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgbuldozer_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgcamerashake_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfglensflare_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgsoundeffects_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgminedetectioncoefs_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgfire_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgirlasersettings_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgfunctions_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgrespawntemplates_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgpostprocesstemplates_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgremoteexeccommands_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgremoteexec_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgcommands_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgorbatdefault_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgeditorcategories_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgeditorsubcategories_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgmuzzleflashes_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgbushnomipmaptextures_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgidentities_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgcuratorchallenges_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfghintcategories_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfghints_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfg3den_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgobjectcompositions_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgcommunicationmenu_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgfiringdrills_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgmusicclasses_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgdestroy_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgmovesanimal_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgmovesbutterfly_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgmovesbird_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgtasks_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgmovesanimal_base_f_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgcommunityguide_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfguicolors_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfguigrids_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfglanguages_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgweaponicons_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgloadingtexts_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgloadingscreens_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgchainofcommand_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgscriptpaths_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgeditorlayouts_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgnotifications_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgdebriefing_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgdlcnotifications_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgunitinsignia_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgholdactions_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgfeedbackeffects_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgmainmenuspotlight_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgmarkerclasses_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgdiarypictures_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgmagazinewells_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgmovesfatigue_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgsentences_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgsfx_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfganimationsourcesounds_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgsoundshapes_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgsoundcurves_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgsoundshaders_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgsoundsets_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgsound3dprocessors_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgdistancefilters_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgsoundglobals_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgsoundcategories_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgarmorsimulations_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgorbat_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgtimetrials_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgvrnomipmaptextures_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgvrcourses_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgradio_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfggroundsupportrequesttypes_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgmarknomipmaptextures_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgrevive_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfghvtobjectives_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgextendedanimation_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgroles_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgargonomipmaptextures_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgleaflets_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
create table if not exists "cfgwlrequisitionpresets_items_tbl" (
    "item_id" integer primary key,
    "item_classname" text not null unique,
    "item_displayname" text,
    "item_inheritance" text,
    "item_mod" text,
    "item_scope" integer,
    "item_type" text,
    "item_descriptionshort" text,
    "item_preview_location" text,
    "item_preview" integer
);
CREATE TABLE IF NOT EXISTS "cfgvehicles_items_tbl" (
    "item_id" integer PRIMARY KEY,
    "item_classname" TEXT NOT NULL UNIQUE,
    "item_displayname" TEXT,
    "item_inheritance" TEXT,
    "item_mod" TEXT,
    "item_scope" INTEGER,
    "item_type" TEXT,
    "item_subtype" TEXT,
    "item_descriptionShort" TEXT,
    "item_preview_location" TEXT,
    "item_preview" INTEGER
);
CREATE TABLE IF NOT EXISTS "cfgweapons_items_tbl" (
    "item_id" INTEGER PRIMARY KEY,
    "item_classname" TEXT NOT NULL UNIQUE,
    "item_displayname" TEXT,
    "item_inheritance" TEXT,
    "item_mod" TEXT,
    "item_scope" INTEGER,
    "item_type" TEXT,
    "item_descriptionshort" TEXT,
    "item_preview_location" TEXT,
    "item_preview" INTEGER
);