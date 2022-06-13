import json
import pandas as pd

with open(r'C:\Users\tonin_work\Documents\Repos\test\New folder\warzone_full_data.json','r') as f:
    data = json.load(f)

# print(data.keys())

attachment_ids=[]

# conflict_ids = []

# attachment_ids = [
#     [gun, data[gun]["PrimaryFireAttachments"][attachment]["LocalizedName"]] 
#     if "PrimaryFireAttachments" in data[gun] else [gun,'NULL']
#     for gun in data 
#     if "LocalizedName" in data[gun]["PrimaryFireAttachments"][attachment] else [gun,'NULL']
#     for attachment in data[gun]["PrimaryFireAttachments"]]

for gun in data:
    if "PrimaryFireAttachments" in data[gun]:
        # if "AttachmentConflicts" in data[gun]: 
        #     conflict_ids.append([gun, data[gun]["AttachmentConflicts"]])

        for attachment in data[gun]["PrimaryFireAttachments"]:
            if "LocalizedName" in data[gun]["PrimaryFireAttachments"][attachment] and ("DamageMultiplier" in data[gun]["PrimaryFireAttachments"][attachment] 
                                                                                    or "DamageMultiplierMultipliers" in data[gun]["PrimaryFireAttachments"][attachment] 
                                                                                    or "DamageOverrides" in data[gun]["PrimaryFireAttachments"][attachment] 
                                                                                    or  "DamageMultiplierOverrides" in data[gun]["PrimaryFireAttachments"][attachment]
                                                                                    ):
                continue
            elif "LocalizedName" in data[gun]["PrimaryFireAttachments"][attachment] and not("DamageMultiplier" in data[gun]["PrimaryFireAttachments"][attachment] 
                                                                                    or "DamageMultiplierMultipliers" in data[gun]["PrimaryFireAttachments"][attachment] 
                                                                                    or "DamageOverrides" in data[gun]["PrimaryFireAttachments"][attachment] 
                                                                                    or  "DamageMultiplierOverrides" in data[gun]["PrimaryFireAttachments"][attachment]
                                                                                    ):
                attachment_ids.append([gun, data[gun]["LocalizedName"], data[gun]["SourceGame"], data[gun]["UIWeaponCategory"], data[gun]["WeaponClass"], attachment, data[gun]["PrimaryFireAttachments"][attachment]["LocalizedName"], data[gun]["PrimaryFireAttachments"][attachment]["AttachmentSlot"]])
            else:
                continue

'''
damagemultiplier
damagemultipliermultipliers
'''

# print(attachment_ids)

df_attachments=pd.DataFrame(attachment_ids,columns=["gun_id", "gun_name", "source_game", "ui_weapon_category", "weapon_class", "attachment_id", "attachment_name", "attachment_slot"])
# df_conflicting_attachments=pd.DataFrame(conflict_ids,columns=["gun_id", "conflicting_attachments"])

# print(df_attachments)
df_attachments.to_excel('Gun_fct_base.xlsx')
# df_conflicting_attachments.to_excel('Conflicts.xlsx')

