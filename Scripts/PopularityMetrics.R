library(effsize)
library(lattice)

graphics.off()
par(mfrow=c(2,1))

data=read.csv("/home/uji657//Downloads/src/HumanAISE2025/Dataset/R_analysis.csv", header = T)


################### Code Files ######################

not_diverse_code_files = data$notD_num_code_files
not_diverse_code_files <- not_diverse[!is.na(not_diverse_code_files) & !is.nan(not_diverse_code_files)]

#summary(delayVio)

# Define the IQR
Q1 = quantile(not_diverse_code_files, 0.25)
Q3 = quantile(not_diverse_code_files, 0.75)
IQR = Q3 - Q1

# Define lower and upper bounds
lower_bound <- Q1 - 1.5 * IQR
upper_bound <- Q3 + 1.5 * IQR

# Remove outliers
not_diverse_code_files <- not_diverse_code_files[not_diverse_code_files >= lower_bound & not_diverse_code_files <= upper_bound]

# Summary of delayVio after removing outliers
summary(not_diverse_code_files)




diverse_code_files = data$D_num_code_files
diverse_code_files <- diverse_code_files[!is.na(diverse_code_files) & !is.nan(diverse_code_files)]

#summary(delayNonVio)

# Define the IQR
Q1 = quantile(diverse, 0.25)
Q3 = quantile(diverse, 0.75)
IQR = Q3 - Q1

# Define lower and upper bounds
lower_bound <- Q1 - 1.5 * IQR
upper_bound <- Q3 + 1.5 * IQR

# Remove outliers
diverse_code_files <- diverse_code_files[diverse_code_files >= lower_bound & diverse_code_files <= upper_bound]

# Summary of delayNonVio after removing outliers
summary(diverse_code_files)


#wilcox.test(delayVio, delayNonVio)

wilcox.test(not_diverse_code_files, diverse_code_files)

cliff.delta(not_diverse_code_files, diverse_code_files)


mean_not_diverse_code_files <- mean(not_diverse_code_files)
mean_diverse_code_files <- mean(diverse_code_files)





################### Code Lines ######################

not_diverse_code_lines = data$notD_total_lines_of_code
not_diverse_code_lines <- not_diverse_code_lines[!is.na(not_diverse_code_lines) & !is.nan(not_diverse_code_lines)]

#summary(delayVio)

# Define the IQR
Q1 = quantile(not_diverse_code_lines, 0.25)
Q3 = quantile(not_diverse_code_lines, 0.75)
IQR = Q3 - Q1

# Define lower and upper bounds
lower_bound <- Q1 - 1.5 * IQR
upper_bound <- Q3 + 1.5 * IQR

# Remove outliers
not_diverse_code_lines <- not_diverse_code_lines[not_diverse_code_lines >= lower_bound & not_diverse_code_lines <= upper_bound]

# Summary of delayVio after removing outliers
summary(not_diverse_code_lines)




diverse_code_lines = data$D_total_lines_of_code
diverse_code_lines <- diverse_code_lines[!is.na(diverse_code_lines) & !is.nan(diverse_code_lines)]

#summary(delayNonVio)

# Define the IQR
Q1 = quantile(diverse_code_lines, 0.25)
Q3 = quantile(diverse_code_lines, 0.75)
IQR = Q3 - Q1

# Define lower and upper bounds
lower_bound <- Q1 - 1.5 * IQR
upper_bound <- Q3 + 1.5 * IQR

# Remove outliers
diverse_code_lines <- diverse_code_lines[diverse_code_lines >= lower_bound & diverse_code_lines <= upper_bound]

# Summary of delayNonVio after removing outliers
summary(diverse_code_lines)


#wilcox.test(delayVio, delayNonVio)

wilcox.test(not_diverse_code_lines, diverse_code_lines)

cliff.delta(not_diverse_code_lines, diverse_code_lines)


mean_not_diverse_code_lines <- mean(not_diverse_code_lines)
mean_diverse_code_lines <- mean(diverse_code_lines)





################### Code modules ######################

not_diverse_code_modules = data$notD_num_modules
not_diverse_code_modules <- not_diverse_code_modules[!is.na(not_diverse_code_modules) & !is.nan(not_diverse_code_modules)]

#summary(delayVio)

# Define the IQR
Q1 = quantile(not_diverse_code_modules, 0.25)
Q3 = quantile(not_diverse_code_modules, 0.75)
IQR = Q3 - Q1

# Define lower and upper bounds
lower_bound <- Q1 - 1.5 * IQR
upper_bound <- Q3 + 1.5 * IQR

# Remove outliers
not_diverse_code_modules <- not_diverse_code_modules[not_diverse_code_modules >= lower_bound & not_diverse_code_modules <= upper_bound]

# Summary of delayVio after removing outliers
summary(not_diverse_code_modules)




diverse_code_modules = data$D_num_modules
diverse_code_modules <- diverse_code_modules[!is.na(diverse_code_modules) & !is.nan(diverse_code_modules)]

#summary(delayNonVio)

# Define the IQR
Q1 = quantile(diverse_code_modules, 0.25)
Q3 = quantile(diverse_code_modules, 0.75)
IQR = Q3 - Q1

# Define lower and upper bounds
lower_bound <- Q1 - 1.5 * IQR
upper_bound <- Q3 + 1.5 * IQR

# Remove outliers
diverse_code_modules <- diverse_code_modules[diverse_code_modules >= lower_bound & diverse_code_modules <= upper_bound]

# Summary of delayNonVio after removing outliers
summary(diverse_code_modules)


#wilcox.test(delayVio, delayNonVio)

wilcox.test(not_diverse_code_modules, diverse_code_modules)

cliff.delta(not_diverse_code_modules, diverse_code_modules)


mean_not_diverse_code_modules <- mean(not_diverse_code_modules)
mean_diverse_code_modules <- mean(diverse_code_modules)



################### Pretrained Models ######################

not_diverse_model = data$notD_pretrained_models
not_diverse_model <- not_diverse_model[!is.na(not_diverse_model) & !is.nan(not_diverse_model)]

#summary(delayVio)

# Define the IQR
Q1 = quantile(not_diverse_model, 0.25)
Q3 = quantile(not_diverse_model, 0.75)
IQR = Q3 - Q1

# Define lower and upper bounds
lower_bound <- Q1 - 1.5 * IQR
upper_bound <- Q3 + 1.5 * IQR

# Remove outliers
not_diverse_model <- not_diverse_model[not_diverse_model >= lower_bound & not_diverse_model <= upper_bound]

# Summary of delayVio after removing outliers
summary(not_diverse_model)




diverse_model = data$D_pretrained_models
diverse_model <- diverse_model[!is.na(diverse_model) & !is.nan(diverse_model)]

#summary(delayNonVio)

# Define the IQR
Q1 = quantile(diverse_model, 0.25)
Q3 = quantile(diverse_model, 0.75)
IQR = Q3 - Q1

# Define lower and upper bounds
lower_bound <- Q1 - 1.5 * IQR
upper_bound <- Q3 + 1.5 * IQR

# Remove outliers
diverse_model <- diverse_model[diverse_model >= lower_bound & diverse_model <= upper_bound]

# Summary of delayNonVio after removing outliers
summary(diverse_model)


#wilcox.test(delayVio, delayNonVio)

wilcox.test(not_diverse_model, diverse_model)

cliff.delta(not_diverse_model, diverse_model)


mean_not_diverse_code_models <- mean(not_diverse_model)
mean_diverse_code_models <- mean(diverse_model)



################### Shell Script ######################

not_diverse_shell_script = data$notD_shell_scripts
not_diverse_shell_script <- not_diverse_shell_script[!is.na(not_diverse_shell_script) & !is.nan(not_diverse_shell_script)]

#summary(delayVio)

# Define the IQR
Q1 = quantile(not_diverse_shell_script, 0.25)
Q3 = quantile(not_diverse_shell_script, 0.75)
IQR = Q3 - Q1

# Define lower and upper bounds
lower_bound <- Q1 - 1.5 * IQR
upper_bound <- Q3 + 1.5 * IQR

# Remove outliers
not_diverse_shell_script <- not_diverse_shell_script[not_diverse_shell_script >= lower_bound & not_diverse_shell_script <= upper_bound]

# Summary of delayVio after removing outliers
summary(not_diverse_shell_script)




diverse_shell_script = data$D_shell_scripts
diverse_shell_script <- diverse_shell_script[!is.na(diverse_shell_script) & !is.nan(diverse_shell_script)]

#summary(delayNonVio)

# Define the IQR
Q1 = quantile(diverse_shell_script, 0.25)
Q3 = quantile(diverse_shell_script, 0.75)
IQR = Q3 - Q1

# Define lower and upper bounds
lower_bound <- Q1 - 1.5 * IQR
upper_bound <- Q3 + 1.5 * IQR

# Remove outliers
diverse_shell_script <- diverse_shell_script[diverse_shell_script >= lower_bound & diverse_shell_script <= upper_bound]

# Summary of delayNonVio after removing outliers
summary(diverse_shell_script)


#wilcox.test(delayVio, delayNonVio)

wilcox.test(not_diverse_shell_script, diverse_shell_script)

cliff.delta(not_diverse_shell_script, diverse_shell_script)


mean_not_diverse_shell_script <- mean(not_diverse_shell_script)
mean_diverse_shell_script <- mean(diverse_shell_script)




################### Lists in README ######################

not_diverse_lists_readme = data$notD_lists_in_readme
not_diverse_lists_readme <- not_diverse_lists_readme[!is.na(not_diverse_lists_readme) & !is.nan(not_diverse_lists_readme)]

#summary(delayVio)

# Define the IQR
Q1 = quantile(not_diverse_lists_readme, 0.25)
Q3 = quantile(not_diverse_lists_readme, 0.75)
IQR = Q3 - Q1

# Define lower and upper bounds
lower_bound <- Q1 - 1.5 * IQR
upper_bound <- Q3 + 1.5 * IQR

# Remove outliers
not_diverse_lists_readme <- not_diverse_lists_readme[not_diverse_lists_readme >= lower_bound & not_diverse_lists_readme <= upper_bound]

# Summary of delayVio after removing outliers
summary(not_diverse_lists_readme)




diverse_lists_readme = data$D_lists_in_readme
diverse_lists_readme <- diverse_lists_readme[!is.na(diverse_lists_readme) & !is.nan(diverse_lists_readme)]

#summary(delayNonVio)

# Define the IQR
Q1 = quantile(diverse_lists_readme, 0.25)
Q3 = quantile(diverse_lists_readme, 0.75)
IQR = Q3 - Q1

# Define lower and upper bounds
lower_bound <- Q1 - 1.5 * IQR
upper_bound <- Q3 + 1.5 * IQR

# Remove outliers
diverse_lists_readme <- diverse_lists_readme[diverse_lists_readme >= lower_bound & diverse_lists_readme <= upper_bound]

# Summary of delayNonVio after removing outliers
summary(diverse_lists_readme)


#wilcox.test(delayVio, delayNonVio)

wilcox.test(not_diverse_lists_readme, diverse_lists_readme)

cliff.delta(not_diverse_lists_readme, diverse_lists_readme)


mean_not_diverse_lists_readme <- mean(not_diverse_lists_readme)
mean_diverse_lists_readme <- mean(diverse_lists_readme)




################### Code Blocks in README ######################

not_diverse_code_blocks_readme = data$notD_code_blocks_in_readme
not_diverse_code_blocks_readme <- not_diverse_code_blocks_readme[!is.na(not_diverse_code_blocks_readme) & !is.nan(not_diverse_code_blocks_readme)]

#summary(delayVio)

# Define the IQR
Q1 = quantile(not_diverse_code_blocks_readme, 0.25)
Q3 = quantile(not_diverse_code_blocks_readme, 0.75)
IQR = Q3 - Q1

# Define lower and upper bounds
lower_bound <- Q1 - 1.5 * IQR
upper_bound <- Q3 + 1.5 * IQR

# Remove outliers
not_diverse_code_blocks_readme <- not_diverse_code_blocks_readme[not_diverse_code_blocks_readme >= lower_bound & not_diverse_code_blocks_readme <= upper_bound]

# Summary of delayVio after removing outliers
summary(not_diverse_code_blocks_readme)




diverse_code_blocks_readme = data$D_code_blocks_in_readme
diverse_code_blocks_readme <- diverse_code_blocks_readme[!is.na(diverse_code_blocks_readme) & !is.nan(diverse_code_blocks_readme)]

#summary(delayNonVio)

# Define the IQR
Q1 = quantile(diverse_code_blocks_readme, 0.25)
Q3 = quantile(diverse_code_blocks_readme, 0.75)
IQR = Q3 - Q1

# Define lower and upper bounds
lower_bound <- Q1 - 1.5 * IQR
upper_bound <- Q3 + 1.5 * IQR

# Remove outliers
diverse_code_blocks_readme <- diverse_code_blocks_readme[diverse_code_blocks_readme >= lower_bound & diverse_code_blocks_readme <= upper_bound]

# Summary of delayNonVio after removing outliers
summary(diverse_code_blocks_readme)


#wilcox.test(delayVio, delayNonVio)

wilcox.test(not_diverse_code_blocks_readme, diverse_code_blocks_readme)

cliff.delta(not_diverse_code_blocks_readme, diverse_code_blocks_readme)


mean_not_diverse_code_blocks_readme <- mean(not_diverse_code_blocks_readme)
mean_diverse_code_blocks_readme <- mean(diverse_code_blocks_readme)


################### Inline codes in README ######################

not_diverse_inline_code_readme = data$notD_inline_code_in_readme
not_diverse_inline_code_readme <- not_diverse_inline_code_readme[!is.na(not_diverse_inline_code_readme) & !is.nan(not_diverse_inline_code_readme)]

#summary(delayVio)

# Define the IQR
Q1 = quantile(not_diverse_inline_code_readme, 0.25)
Q3 = quantile(not_diverse_inline_code_readme, 0.75)
IQR = Q3 - Q1

# Define lower and upper bounds
lower_bound <- Q1 - 1.5 * IQR
upper_bound <- Q3 + 1.5 * IQR

# Remove outliers
not_diverse_inline_code_readme <- not_diverse_inline_code_readme[not_diverse_inline_code_readme >= lower_bound & not_diverse_inline_code_readme <= upper_bound]

# Summary of delayVio after removing outliers
summary(not_diverse_inline_code_readme)




diverse_inline_code_readme = data$D_inline_code_in_readme
diverse_inline_code_readme <- diverse_inline_code_readme[!is.na(diverse_inline_code_readme) & !is.nan(diverse_inline_code_readme)]

#summary(delayNonVio)

# Define the IQR
Q1 = quantile(diverse_inline_code_readme, 0.25)
Q3 = quantile(diverse_inline_code_readme, 0.75)
IQR = Q3 - Q1

# Define lower and upper bounds
lower_bound <- Q1 - 1.5 * IQR
upper_bound <- Q3 + 1.5 * IQR

# Remove outliers
diverse_inline_code_readme <- diverse_inline_code_readme[diverse_inline_code_readme >= lower_bound & diverse_inline_code_readme <= upper_bound]

# Summary of delayNonVio after removing outliers
summary(diverse_inline_code_readme)


#wilcox.test(delayVio, delayNonVio)

wilcox.test(not_diverse_inline_code_readme, diverse_inline_code_readme)

cliff.delta(not_diverse_inline_code_readme, diverse_inline_code_readme)


mean_not_diverse_inline_code_readme <- mean(not_diverse_inline_code_readme)
mean_diverse_inline_code_readme <- mean(diverse_inline_code_readme)




################### Images in README ######################

not_diverse_images_readme = data$notD_images_in_readme
not_diverse_images_readme <- not_diverse_images_readme[!is.na(not_diverse_images_readme) & !is.nan(not_diverse_images_readme)]

#summary(delayVio)

# Define the IQR
Q1 = quantile(not_diverse_images_readme, 0.25)
Q3 = quantile(not_diverse_images_readme, 0.75)
IQR = Q3 - Q1

# Define lower and upper bounds
lower_bound <- Q1 - 1.5 * IQR
upper_bound <- Q3 + 1.5 * IQR

# Remove outliers
not_diverse_images_readme <- not_diverse_images_readme[not_diverse_images_readme >= lower_bound & not_diverse_images_readme <= upper_bound]

# Summary of delayVio after removing outliers
summary(not_diverse_images_readme)




diverse_images_readme = data$D_images_in_readme
diverse_images_readme <- diverse_images_readme[!is.na(diverse_images_readme) & !is.nan(diverse_images_readme)]

#summary(delayNonVio)

# Define the IQR
Q1 = quantile(diverse_images_readme, 0.25)
Q3 = quantile(diverse_images_readme, 0.75)
IQR = Q3 - Q1

# Define lower and upper bounds
lower_bound <- Q1 - 1.5 * IQR
upper_bound <- Q3 + 1.5 * IQR

# Remove outliers
diverse_images_readme <- diverse_images_readme[diverse_images_readme >= lower_bound & diverse_images_readme <= upper_bound]

# Summary of delayNonVio after removing outliers
summary(diverse_images_readme)


#wilcox.test(delayVio, delayNonVio)

wilcox.test(not_diverse_images_readme, diverse_images_readme)

cliff.delta(not_diverse_images_readme, diverse_images_readme)


mean_not_diverse_images_readme <- mean(not_diverse_images_readme)
mean_diverse_images_readme <- mean(diverse_images_readme)






################### GitHub Links in README ######################

not_diverse_github_readme = data$notD_github_links_in_readme
not_diverse_github_readme <- not_diverse_github_readme[!is.na(not_diverse_github_readme) & !is.nan(not_diverse_github_readme)]

#summary(delayVio)

# Define the IQR
Q1 = quantile(not_diverse_github_readme, 0.25)
Q3 = quantile(not_diverse_github_readme, 0.75)
IQR = Q3 - Q1

# Define lower and upper bounds
lower_bound <- Q1 - 1.5 * IQR
upper_bound <- Q3 + 1.5 * IQR

# Remove outliers
not_diverse_github_readme <- not_diverse_github_readme[not_diverse_github_readme >= lower_bound & not_diverse_github_readme <= upper_bound]

# Summary of delayVio after removing outliers
summary(not_diverse_github_readme)




diverse_github_readme = data$D_github_links_in_readme
diverse_github_readme <- diverse_github_readme[!is.na(diverse_github_readme) & !is.nan(diverse_github_readme)]

#summary(delayNonVio)

# Define the IQR
Q1 = quantile(diverse_github_readme, 0.25)
Q3 = quantile(diverse_github_readme, 0.75)
IQR = Q3 - Q1

# Define lower and upper bounds
lower_bound <- Q1 - 1.5 * IQR
upper_bound <- Q3 + 1.5 * IQR

# Remove outliers
diverse_github_readme <- diverse_github_readme[diverse_github_readme >= lower_bound & diverse_github_readme <= upper_bound]

# Summary of delayNonVio after removing outliers
summary(diverse_github_readme)


#wilcox.test(delayVio, delayNonVio)

wilcox.test(not_diverse_github_readme, diverse_github_readme)

cliff.delta(not_diverse_github_readme, diverse_github_readme)


mean_not_diverse_github_readme <- mean(not_diverse_github_readme)
mean_diverse_github_readme <- mean(diverse_github_readme)





################### License ######################

not_diverse_license = data$notD_has_license
not_diverse_license <- not_diverse_license[!is.na(not_diverse_license) & !is.nan(not_diverse_license)]

#summary(delayVio)

# Define the IQR
Q1 = quantile(not_diverse_license, 0.25)
Q3 = quantile(not_diverse_license, 0.75)
IQR = Q3 - Q1

# Define lower and upper bounds
lower_bound <- Q1 - 1.5 * IQR
upper_bound <- Q3 + 1.5 * IQR

# Remove outliers
not_diverse_license <- not_diverse_license[not_diverse_license >= lower_bound & not_diverse_license <= upper_bound]

# Summary of delayVio after removing outliers
summary(not_diverse_license)




diverse_license = data$D_has_license
diverse_license <- diverse_license[!is.na(diverse_license) & !is.nan(diverse_license)]

#summary(delayNonVio)

# Define the IQR
Q1 = quantile(diverse_license, 0.25)
Q3 = quantile(diverse_license, 0.75)
IQR = Q3 - Q1

# Define lower and upper bounds
lower_bound <- Q1 - 1.5 * IQR
upper_bound <- Q3 + 1.5 * IQR

# Remove outliers
diverse_license <- diverse_license[diverse_license >= lower_bound & diverse_license <= upper_bound]

# Summary of delayNonVio after removing outliers
summary(diverse_license)


#wilcox.test(delayVio, delayNonVio)

wilcox.test(not_diverse_license, diverse_license)

cliff.delta(not_diverse_license, diverse_license)


mean_not_diverse_license <- mean(not_diverse_license)
mean_diverse_license <- mean(diverse_license)




boxplot(not_diverse_code_files, diverse_code_files, 
        not_diverse_code_lines, diverse_code_lines, 
        not_diverse_code_modules, diverse_code_modules,
        not_diverse_model, diverse_model, 
        not_diverse_shell_script, diverse_shell_script, 
        not_diverse_lists_readme, diverse_lists_readme,
        at=c(1,2,  4,5,  7,8,  10,11,  13,14,  16,17), 
        xaxt="n", 
        ylab="Popularity Metrics", 
        outline = F,
        cex.lab=0.9,
        col = c(
          "gray","white",
          "gray","white", 
          "gray","white", 
          "gray","white", 
          "gray","white" , 
          "gray","white"
        )
)
axis(side=1,
     at=c(1.5, 4.5, 7.5, 10.5, 13.5, 16.5),  
     labels= c("# of lines of code", 
               "# of lines of code", 
               "# of code modules", 
               "# of pretrained models", 
               "# of shell scripts", 
               "# of lists in README"), 
     cex.axis = 0.75
)

abline(v=3, lty=2)
abline(v=6, lty=2)
abline(v=9, lty=2)
abline(v=12, lty=2)
abline(v=15, lty=2)
abline(v=18, lty=2)

points(c(1,2,  4,5,  7,8,  10,11, 13,14,  16,17), 
       c(
         mean_not_diverse_code_files, mean_diverse_code_files, 
         mean_not_diverse_code_lines, mean_diverse_code_lines, 
         mean_not_diverse_code_modules, mean_diverse_code_modules, 
         mean_not_diverse_code_models, mean_diverse_code_models, 
         mean_not_diverse_shell_script, mean_diverse_shell_script, 
         mean_not_diverse_lists_readme, mean_diverse_lists_readme
       ),
       col = "black", 
       pch = 19)

text(x = c(1,2,  4,5,  7,8,  10,11, 13,14,  16,17), 
     y = c(
       mean_not_diverse_code_files, mean_diverse_code_files, 
       mean_not_diverse_code_lines, mean_diverse_code_lines,
       mean_not_diverse_code_modules, mean_diverse_code_modules, 
       mean_not_diverse_code_models, mean_diverse_code_models, 
       mean_not_diverse_shell_script, mean_diverse_shell_script, 
       mean_not_diverse_lists_readme, mean_diverse_lists_readme
     ), 
     labels = paste(round(c(
       mean_not_diverse_code_files, mean_diverse_code_files, 
       mean_not_diverse_code_lines, mean_diverse_code_lines, 
       mean_not_diverse_code_modules, mean_diverse_code_modules, 
       mean_not_diverse_code_models, mean_diverse_code_models, 
       mean_not_diverse_shell_script, mean_diverse_shell_script, 
       mean_not_diverse_lists_readme, mean_diverse_lists_readme),
     2)), 
     pos = 3, 
     cex=0.80,
     col = "black")

legend("topright", 
       legend = c("Not-diverse", "diverse"), 
       col = c("black", "gray"), 
       cex = 0.7,               # Text size
       pt.cex = 0.8,             # Point size
       pch = c(0, 15),           # Symbols for Female and Male
       x.intersp = 0.5,         # Horizontal space between legend text and symbols
       y.intersp = 0.75,          # Vertical space between legend items
       box.col = "black",        # Box color
       bg = "white")  







boxplot(
        not_diverse_code_blocks_readme, diverse_code_blocks_readme,
        not_diverse_inline_code_readme, diverse_inline_code_readme,
        not_diverse_images_readme, diverse_images_readme,
        not_diverse_github_readme, diverse_github_readme,
        not_diverse_license, diverse_license,
        at=c(1,2,  4,5,  7,8,  10,11,  13,14), 
        xaxt="n", 
        ylab="Popularity Metrics", 
        outline = F,
        cex.lab=0.9,
        col = c(
          "gray","white",
          "gray","white", 
          "gray","white", 
          "gray","white", 
          "gray","white"
          )
        )
axis(side=1,
     at=c(1.5, 4.5, 7.5, 10.5, 13.5),  
     labels= c("# of code blocks in README", 
               "# of inline code in README", 
               "# of images in README", 
               "# of github links in README", 
               "has license?"
            ), 
     cex.axis = 0.75
     )

abline(v=3, lty=2)
abline(v=6, lty=2)
abline(v=9, lty=2)
abline(v=12, lty=2)
abline(v=15, lty=2)


points(c(1,2,  4,5,  7,8,  10,11, 13,14), 
       c(
         mean_not_diverse_code_blocks_readme, mean_diverse_code_blocks_readme,
         mean_not_diverse_inline_code_readme, mean_diverse_inline_code_readme,
         mean_not_diverse_images_readme, mean_diverse_images_readme,
         mean_not_diverse_github_readme, mean_diverse_github_readme, 
         mean_not_diverse_license, mean_diverse_license
         ),
       col = "black", 
       pch = 19)

text(x = c(1,2,  4,5,  7,8,  10,11, 13,14), 
     y = c(
      mean_not_diverse_code_blocks_readme, mean_diverse_code_blocks_readme,
       mean_not_diverse_inline_code_readme, mean_diverse_inline_code_readme,
       mean_not_diverse_images_readme, mean_diverse_images_readme,
       mean_not_diverse_github_readme, mean_diverse_github_readme, 
       mean_not_diverse_license, mean_diverse_license
           ), 
     labels = paste(round(c(
       mean_not_diverse_code_blocks_readme, mean_diverse_code_blocks_readme,
       mean_not_diverse_inline_code_readme, mean_diverse_inline_code_readme,
       mean_not_diverse_images_readme, mean_diverse_images_readme,
       mean_not_diverse_github_readme, mean_diverse_github_readme, 
       mean_not_diverse_license, mean_diverse_license
       ),
     2)), 
     pos = 3, 
     cex=0.80,
     col = "black")

legend("topright", 
       legend = c("Not-diverse", "diverse"), 
       col = c("black", "gray"), 
       cex = 0.7,               # Text size
       pt.cex = 0.8,             # Point size
       pch = c(0, 15),           # Symbols for Female and Male
       x.intersp = 0.5,         # Horizontal space between legend text and symbols
       y.intersp = 0.75,          # Vertical space between legend items
       box.col = "black",        # Box color
       bg = "white") 

